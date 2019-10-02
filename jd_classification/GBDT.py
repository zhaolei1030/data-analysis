from sklearn import ensemble
import numpy as np
from sklearn.metrics import accuracy_score
from time import time
import sklearn
# 包含的参数
# loss = loss, learning_rate = learning_rate, n_estimators = n_estimators,
# min_samples_split = min_samples_split,
# min_samples_leaf = min_samples_leaf,
# min_weight_fraction_leaf = min_weight_fraction_leaf,
# max_depth = max_depth, init = init, subsample = subsample,
# max_features = max_features,
# random_state = random_state, verbose = verbose,
# max_leaf_nodes = max_leaf_nodes, warm_start = warm_start,
# presort = presort
data = np.loadtxt(open("path\\test(100).csv","rb"),delimiter=",",skiprows=0)
x, y = np.split(data, (100,), axis=1)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, random_state=1, train_size=0.8)
y_tra = y_train.ravel().astype(np.int)

clf = ensemble.GradientBoostingClassifier(loss= 'deviance',learning_rate = 0.001)
# clf.fit(x_train, y_train)  # Training model
# predicty_x = gbdt_model.predict_proba(test1217_x)[:, 1]  # predict: probablity of 1
t1 = time()
clf.fit(x_train, y_tra)
t2 = time()
t = t2 - t1
print('GBDT训练模型耗时：%d分%.3f秒' % ((int)(t / 60), t - 60 * (int)(t / 60)))
y_hat1 = clf.predict(x_test)
print('GBDT训练集准确率：', accuracy_score(y_train, clf.predict(x_train)))
print('GBDT测试集准确率：', accuracy_score(y_test, y_hat1))
print('*************************')