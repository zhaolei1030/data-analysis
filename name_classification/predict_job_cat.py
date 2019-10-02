from svm_classify import profession_predict
with open('./data/job_cat.txt', encoding='utf-8')as f:
    with open('./data/job_cat_ret.txt', 'w', encoding='utf-8')as f2:
        for i in f:
            line = i.strip()
            ret = profession_predict(line)
            ret = line+': ' + str(ret[0]) + '\n'
            f2.write(ret)