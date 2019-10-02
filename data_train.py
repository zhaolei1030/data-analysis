import xlrd
import time
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

def extract_Data(file):
    """
    提取数据
    :param file:
    :return:
    """
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows
    f_list = []
    c_list = []
    s_list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        f_list.append(row[4])
        c_list.append(row[5])
        s_list.append(row[6])
    return f_list,c_list,s_list
def load_Data(f_list, c_list, s_list):
    c = np.array([c_list])
    cmin, cmax = c.min(), c.max()
    # c_mean = np.mean(c)
    c_scaled = (c - cmin) / (cmax - cmin)
    s = np.array([s_list])
    smin, smax = s.min(), s.max()
    # s_mean = np.mean(s)
    s_scaled = (s - cmin) / (smax - smin)
    # x = np.row_stack((c_scaled, s_scaled))
    x = np.row_stack((c_scaled, s_scaled))
    X = x.T
    f = np.array([f_list])
    fmin, fmax = f.min(), f.max()
    f_scaled = (f - cmin) / (fmax - fmin)
    Y = f_scaled.T
    Y = Y.reshape(Y.shape[0],)
    num = X.shape[0]
    num = int(num*0.8)
    return X[:num], Y[:num], X[num+1:], Y[num+1:]

if __name__ =="__main__":
    f_list = []
    c_list = []
    s_list = []
    c_test = []
    s_test = []
    f_list, c_list, s_list= extract_Data("./data/train_final_1.xlsx")
    _, c_test, s_test = extract_Data("./data/test_final_1.xlsx")
    x_train, y_train, x_test, y_test = load_Data(f_list, c_list, s_list)
    # print(y_test)
    # print(y_test.shape)
    t0 = time.time()
    poly_reg = PolynomialFeatures(degree=9)
    x_train_poly = poly_reg.fit_transform(x_train)
    x_test_poly = poly_reg.fit_transform(x_test)
    lin_reg_2 = LinearRegression()
    print("开始训练")
    lin_reg_2.fit(x_train_poly, y_train)
    # print(y_train)
    # svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,  param_grid={"C": [1e0, 1e1, 1e2, 1e3], "gamma": np.logspace(-2, 2, 5)})
    # svr.fit(x_train, y_train)
    svm_fit = time.time() - t0
    t0 = time.time()
    y_linear = lin_reg_2.predict(x_test_poly)
    svm_predict = time.time() - t0

    print("\n训练时间：{} 秒\n".format(svm_fit))
    print("\n预测时间： 秒\n".format(svm_predict))
    print('loss = {}'.format(np.sum(np.fabs(y_test - y_linear))/y_linear.shape[0]))
    # print(x_test[:,0].shape)
    # print(y_svr.shape)
    x = np.arange(y_linear.shape[0])
    plt.figure()
    plt.plot(x, y_linear)
    plt.plot(x, y_test, color='blue', linewidth=3.0, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
