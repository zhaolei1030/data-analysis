import matplotlib.pyplot as plt
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.python.framework import ops
from tf_utils import load_dataset, random_mini_batches, convert_to_one_hot, predict
import numpy as np
np.random.seed(1)
def sigmoid(z):
    x = tf.placeholder(tf.float32, name = "x")
    sigmoid = tf.sigmoid(x)
    with tf.Session() as sess:
        result = sess.run(sigmoid,feed_dict={x:z})
    return result
def cost(logits, labels):
    z = tf.placeholder(tf.float32, name="z")
    y = tf.placeholder(tf.float32, name="y")
    cost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
    sess = tf.Session()
    cost = sess.run(cost, feed_dict={z: logits, y: labels})
    sess.close()
    return cost
def one_hot_matrix(labels, C):
    C = tf.constant(C, name = "C")
    one_hot_matrix = tf.one_hot(labels, C, axis=0)
    sess = tf.Session()
    one_hot = sess.run(one_hot_matrix)
    sess.close()
    return one_hot
def ones(shape):
    ones = tf.ones(shape)
    sess = tf.Session()
    ones = sess.run(ones)
    sess.close()
    return ones
data = np.loadtxt(open("path\\test.csv","rb"),delimiter=",",skiprows=0)
train_data = data[:-10000,:].T
test_data1 = data[-10000:,:].T
# test_data2 = data[-2000:,:].T
X_train = train_data[:300,:]
Y_train = train_data[300,0:].reshape((1,-1))
X_train = X_train
X_test = test_data1[:300,:]
Y_test = test_data1[300].reshape((1,-1))
# X_test = np.hstack((test_data1[:300,:],test_data2[:300,:]))
# Y_test = np.hstack((test_data1[300],test_data2[300])).reshape((1,-1))
# X_train = (X_train - np.mean(X_train,axis=1))/(X_train.max(1) - X_train.min(1))
# X_test = (X_test - np.mean(X_test,axis=1))/(X_test.max(1) - X_test.min(1))
for i in range(300):
    X_train[i] = (X_train[i] - np.mean(X_train[i]))/(np.mean(X_train[i]) - np.max(X_train[i]))
    X_test[i] = (X_test[i] - np.mean(X_test[i])) / (np.mean(X_test[i]) - np.max(X_test[i]))
print(Y_test)

def create_placeholders(n_x, n_y):
    X = tf.placeholder(shape=[n_x, None],dtype=tf.float32)
    Y = tf.placeholder(shape=[n_y, None],dtype=tf.float32)
    return X, Y
def initialize_parameters():
    """
    初始化向量
    :return:
    """
    tf.set_random_seed(1)
    W1 = tf.get_variable("W1", [25,300], initializer =
                            tf.contrib.layers.xavier_initializer(seed = 1))
    b1 = tf.get_variable("b1", [25,1], initializer = tf.zeros_initializer())

    W2 = tf.get_variable("W2", [12,25], initializer =
                            tf.contrib.layers.xavier_initializer(seed = 1))
    b2 = tf.get_variable("b2", [12,1], initializer = tf.zeros_initializer())

    W3 = tf.get_variable("W3", [1,12], initializer =
                            tf.contrib.layers.xavier_initializer(seed = 1))
    b3 = tf.get_variable("b3", [1,1], initializer = tf.zeros_initializer())
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2,
                  "W3": W3,
                  "b3": b3}
    return parameters

def forward_propagation(X, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    W3 = parameters['W3']
    b3 = parameters['b3']

    Z1 = tf.add(tf.matmul(W1,X),b1)            # Z1 = np.dot(W1, X) + b1
    A1 = tf.nn.relu(Z1)                        # A1 = relu(Z1)
    Z2 = tf.add(tf.matmul(W2,A1),b2)           # Z2 = np.dot(W2, a1) + b2
    A2 = tf.nn.relu(Z2)                        # A2 = relu(Z2)
    Z3 = tf.add(tf.matmul(W3,A2),b3)           # Z3 = np.dot(W3,Z2) + b3

    return Z3

def compute_cost(Z3, Y):
    logits = tf.transpose(Z3)
    labels = tf.transpose(Y)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = labels))

    return cost

def model(X_train, Y_train, X_test, Y_test, learning_rate = 0.00001,
          num_epochs = 25, minibatch_size = 32, print_cost = True):
    """
    调用函数进行训练
    :param X_train:
    :param Y_train:
    :param X_test:
    :param Y_test:
    :param learning_rate:
    :param num_epochs:
    :param minibatch_size:
    :param print_cost:
    :return:
    """
    ops.reset_default_graph()
    tf.set_random_seed(1)
    seed = 3
    (n_x, m) = X_train.shape
    n_y = Y_train.shape[0]
    costs = []
    X, Y = create_placeholders(n_x, n_y)
    parameters = initialize_parameters()
    Z3 = forward_propagation(X, parameters)
    cost = compute_cost(Z3, Y)
    optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for epoch in range(num_epochs):
            epoch_cost = 0.
            num_minibatches = int(m / minibatch_size)
            seed = seed + 1
            minibatches = random_mini_batches(X_train, Y_train, minibatch_size, seed)
            for minibatch in minibatches:
                (minibatch_X, minibatch_Y) = minibatch
                _ , minibatch_cost = sess.run([optimizer, cost], feed_dict=
                                                        {X: minibatch_X, Y: minibatch_Y})
                print(minibatch_cost)
                epoch_cost += minibatch_cost / num_minibatches
            if print_cost == True and epoch % 15 == 0:
                print ("Cost after epoch %i: %f" % (epoch, epoch_cost))
            if print_cost == True and epoch % 5 == 0:
                costs.append(epoch_cost)
        plt.plot(np.squeeze(costs))
        plt.ylabel('损失')
        plt.xlabel('迭代 ')
        plt.title("学习率" + str(learning_rate))
        plt.show()
        parameters = sess.run(parameters)
        correct_prediction = tf.equal(tf.argmax(Z3), tf.argmax(Y))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print ("训练集学习率:", accuracy.eval({X: X_train, Y: Y_train}))
        print ("测试集学习率:", accuracy.eval({X: X_test, Y: Y_test}))
        return parameters

if __name__ == '__main__':
    parameters = model(X_train, Y_train, X_test, Y_test)