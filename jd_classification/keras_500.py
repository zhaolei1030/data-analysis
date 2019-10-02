import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

# fix random seed for reproducibility
seed = 9
np.random.seed(seed)
data = np.loadtxt(open("path\position_4(300).csv","rb"),delimiter=",",skiprows=0)
# print(data.shape)
x = data[:,0:300]
y = data[:,301]
print(y.shape)
# y = (y == 5)
train_X, test_X, train_y, test_y = train_test_split(x, y, train_size=0.8, random_state=0)
for i in range(300):
    x[:,i] = (x[:,i] - np.mean(x[:,i]))/(np.mean(x[:,i]) - np.max(x[:,i]))
# for i in range(300):
#     train_X[i] = (train_X[i] - np.mean(train_X[i]))/(np.mean(train_X[i]) - np.max(train_X[i]))
#     test_X[i] = (test_X[i] - np.mean(test_X[i])) / (np.mean(test_X[i]) - np.max(test_X[i]))
# print(x[:,2])
def one_hot_encode_object_array(arr):
    """
    去重并排序
    :param arr:
    :return:
    """
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))
train_y_ohe = one_hot_encode_object_array(train_y)
test_y_ohe = one_hot_encode_object_array(test_y)
model = Sequential()
model.add(Dense(256, input_shape=(300,)))
model.add(Activation('relu'))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
# model.compile( loss='categorical_crossentropy', metrics=["accuracy"],optimizer = keras.optimizers.Adam(lr=0.00001, beta_1=0.9, beta_2=0.999, epsilon=1e-8) )
model.compile( loss='binary_crossentropy', metrics=["accuracy"],optimizer = keras.optimizers.Adam(lr=0.0001, epsilon=1e-08) )
losses = []
for i in range(100):
    model.fit(train_X, train_y, epochs=5, batch_size=50, verbose=0)
    # model.fit(train_X, train_y_ohe, epochs=10, batch_size=50, verbose=0)
    loss, accuracy = model.evaluate(test_X, test_y, verbose=0)
    # loss, accuracy = model.evaluate(test_X, test_y_ohe, verbose=0)
    print("Accuracy = {:.2f}".format(accuracy))
    print(loss)
    losses.append(loss)
plt.plot(losses)
plt.show()
model.save('model4.h5')
#model.compile( loss='binary_crossentropy', metrics=["accuracy"],optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08) )(文件2准确率0.97，样本1.6w)(五层)
#model.compile( loss='binary_crossentropy', metrics=["accuracy"],optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08) )(文件4准确率0.82，样本1281)(五层)
#model.compile( loss='binary_crossentropy', metrics=["accuracy"],optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08) )(文件5准确率0.91，样本8058)(五层)
