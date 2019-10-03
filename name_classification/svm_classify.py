import re
import jieba
from sklearn.externals import joblib
from sklearn.svm import SVC

def create_train_data():
    """构建训练集特征向量numpy_out_li
       以及标签向量feature_li
    """
    jieba.load_userdict('./data/user_dict.txt')
    with open('./data/job_classification.yml', 'r', encoding='utf-8') as f1:
        with open('./data/bag_of_words.txt', 'r', encoding='utf-8') as f2:
            pure_di = eval(f2.read())
            vec_length = len(pure_di)
            # print(vec_length)
            numpy_out_li = list()
            feature_li = list()
            for i in f1:
                line = i.strip().lower().split(': ')[0]
                class_line = i.strip().lower().split(': ')[1]
                line_li = list(jieba.cut_for_search(line))
                feature_li.append(class_line)

                line_str2 = re.sub(r'…|/|\(|\)|\.|）|（', '', ' '.join(line_li))

                line_li_new = [i for i in line_str2.split(' ') if len(i) > 0]## 对IT研发总监: C01中前面那一部分的进行拆分，得到前面那一部分

                # numpy_in_li: [170, 104, 305, 221] -->数字代表第几个位置的向量的数字应该为1
                numpy_in_li = [pure_di.get(k, None) for k in line_li_new]  ##找到'文档': 1, '策划': 2, '验证': 3, '家用': 4,  中相应词的位置

                in_vec_li = [1 if num in numpy_in_li else 0 for num in range(1, vec_length + 1)]

                numpy_out_li.append(in_vec_li)

    # print(numpy_out_li)
    # print(feature_li)
    return numpy_out_li, feature_li   #返回的是两个在一开始提到的向量


def fit_train_data(train_li, feat_li):
    """
    训练模型，保存模型，查看模型准确率
    :param train_li: 特征值
    :param feat_li:标签值
    :return:
    """
    print(train_li)
    print(len(train_li))
    print(len(feat_li))
    print(feat_li)

    model = SVC(kernel='linear', C=100)
    model.fit(X=train_li, y=feat_li)
    joblib.dump(model, "./data/model/train_model.model")
    
    # 检验结果的准确率：通过预测训练集
    # y_pred = model.predict(train_li)
    # print('多输出多分类器预测输出分类:\n', y_pred)
    # n = 0
    # for i in range(len(feat_li)):
    #     if feat_li[i] == y_pred[i]:
    #         n += 1
    # print(n)
    # print(float(n / len(feat_li)))


def profession_predict(name):
    """预测岗位的职能
       1.构建岗位的特征向量
       2.预测岗位的职能
    """
    jieba.load_userdict('./data/user_dict.txt')
    with open('./data/bag_of_words.txt', 'r', encoding='utf-8') as f2:
        pure_di = eval(f2.read())
        vec_length = len(pure_di)
        # print(vec_length)
        li = list(jieba.cut_for_search(name.lower()))
        # print(li)
        line_str2 = re.sub(r'…|/|\(|\)|\.|）|（', '', ' '.join(li))

        line_li_new = [i for i in line_str2.split(' ') if len(i) > 0]

        numpy_in_li = [pure_di.get(i, None) for i in line_li_new]

        in_vec_li = [1 if num in numpy_in_li else 0 for num in range(1, vec_length + 1)]

    model = joblib.load("./data/model/train_model.model")
    predicted = model.predict([in_vec_li])

    return predicted


if __name__ == '__main__':
    # train, features = create_train_data()

    # fit_train_data(train, features)

    ret = profession_predict('架构师')
    print(ret)
