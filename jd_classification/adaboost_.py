import numpy as np
from sklearn.metrics import accuracy_score
from time import time
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn

data = np.loadtxt(open("path/test(100).csv","rb"),delimiter=",",skiprows=0)
x, y = np.split(data, (100,), axis=1)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, random_state=1, train_size=0.8)
y_tra = y_train.ravel().astype(np.int)

clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=10, min_samples_split=5, min_samples_leaf=100), n_estimators=200,
                         learning_rate=0.05, algorithm='SAMME.R')
t1 = time()
clf.fit(x_train, y_tra)
t2 = time()
t = t2 - t1
print('AdaBoost-DT训练模型耗时：{}分' .format((int)(t / 60)))
y_hat1 = clf.predict(x_test)
print('AdaBoost-DT训练集准确率：', accuracy_score(y_tra, clf.predict(x_train)))
print('AdaBoost-DT测试集准确率：', accuracy_score(y_test, y_hat1))
