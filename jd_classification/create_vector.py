import numpy as np
import csv
import gensim
import jieba
import json as js
from gensim.models.doc2vec import Doc2Vec
TaggededDocument = gensim.models.doc2vec.TaggedDocument
text = []
with open('D:\path\\vecor_train_text.txt',encoding='utf-8')as f:
    for line in f:
        text.append(line)
def cut_sentence(text):
    """
    切分句子
    :param text:
    :return:
    """
    result = []
    for each in text:
        each_cut = jieba.cut(each)
        each_split = ' '.join(each_cut).split()
        each_result = [word for word in each_split]
        result.append(each_result)
    return  result
b = cut_sentence(text)
def X_train(cut_sentence):
    """
    得到句子训练集的数据
    :param cut_sentence:
    :return:
    """
    X_train = []
    for i,text in enumerate(cut_sentence):
        word_list = str(text).split()
        l = len(word_list)
        word_list[l-1] = word_list[l-1].strip()
        doucment = TaggededDocument(word_list,tags=[i])
        X_train.append(doucment)
    return X_train
c = X_train(b)
def train(x_train,size = 300):
    """
    对训练集数据训练成模型
    :param x_train:
    :param size:
    :return:
    """
    model = Doc2Vec(x_train,min_count =1,window=3,size = size,sample = 1e-3,negative=10,workers=8)
    model.train(x_train,total_examples=model.corpus_count,epochs=10)
    return model
model_dm = train(c)

def creat_vector(i):
    """
    创建词向量
    :param i:
    :return:
    """
    vector = model_dm.infer_vector(doc_words=i,alpha=0.025,steps=100)
    return vector
count = 0
with open('path\\total_test_have_position.json',encoding='utf-8')as f:
    out = open('position_test(300).csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    for i in f:
        count += 1
        i = js.loads(i)
        if "job_position" in i.keys():
            if 'job_duty' in i.keys():
                a = ','.join(i['job_duty'])
            else:
                a = ''
            if 'job_skill' in i.keys():
                b = ','.join(i['job_skill'])
            else:
                b = ''
            if c != '':
                c = jieba.cut(a+b)
                c = ' '.join(c).split()
                i['vector'] = creat_vector(a+b)
                if count % 500 == 0:
                    print(count)
                if 'class' not in i.keys():
                    continue
                c = np.append(i['vector'],i['class'])
                c = np.append(c,i['job_position'])
                if i['class'] == 0:
                    print(i)
                csv_write.writerow(c)