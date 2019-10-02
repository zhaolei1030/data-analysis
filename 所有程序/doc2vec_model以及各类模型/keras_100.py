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

import time
# fix random seed for reproducibility
seed = 9
np.random.seed(seed)
data = np.loadtxt(open("D:\work(finance)\doc2vec_model\position_test(100).csv","rb"),delimiter=",",skiprows=0)
x = data[:,0:100]
y = data[:,100]
print(data.shape)
print(y.shape)
y = (y == 1)
train_X, test_X, train_y, test_y = train_test_split(x, y, train_size=0.8, random_state=0)
for i in range(100):
    x[:,i] = (x[:,i] - np.mean(x[:,i]))/(np.mean(x[:,i]) - np.max(x[:,i]))
# for i in range(300):
#     train_X[i] = (train_X[i] - np.mean(train_X[i]))/(np.mean(train_X[i]) - np.max(train_X[i]))
#     test_X[i] = (test_X[i] - np.mean(test_X[i])) / (np.mean(test_X[i]) - np.max(test_X[i]))
def one_hot_encode_object_array(arr):
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))
train_y_ohe = one_hot_encode_object_array(train_y)
test_y_ohe = one_hot_encode_object_array(test_y)
model = Sequential()
model.add(Dense(88, input_shape=(100,)))
model.add(Activation('sigmoid'))
model.add(Dense(64))
model.add(Activation('sigmoid'))
model.add(Dense(49))
model.add(Activation('sigmoid'))
model.add(Dense(16))
model.add(Activation('sigmoid'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer = keras.optimizers.Adam(lr=0.0001, epsilon=1e-08), metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
losses = []
for i in range(300):
    model.fit(train_X, train_y, epochs=5, batch_size=50, verbose=0)
    loss, accuracy = model.evaluate(test_X, test_y, verbose=0)
    # loss, accuracy = model.evaluate(test_X, test_y_ohe, verbose=0)
    print("Accuracy = {:.2f}".format(accuracy))
    losses.append(loss)
    print(loss)
plt.plot(losses)
plt.show()
# model.save('indus_model1.h5')