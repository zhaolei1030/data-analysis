import jieba
import re


def create_data():
    """创建模型需要的基础数据，原始数据为job.txt
       生成的数据：bag_of_words.txt，构建词袋，并给每个词一个编号
    """
    # 加载用户字典
    jieba.load_userdict('path/data/user_dict.txt')
    with open('path/data/job.txt', encoding='utf-8') as f:
        with open('path/data/bag_of_words.txt', 'w', encoding='utf-8') as f2:
            # 所有的词
            all_li = list()
            # 每行的词，并用空格隔开
            all_str_li = list()
            for i in f:
                line = i.strip().lower()
                if line[0] == '*':
                    # print(line)
                    line_li = list(jieba.cut_for_search(line[1:]))
                    # print(line_li)
                    line_str = ' '.join(line_li)
                    line_str = re.sub(r'…|/|\(|\)|\.|）|（', '', line_str)
                    all_str_li.append(line_str)
                    line_lis = line_str.split(' ')
                    for k in line_lis:
                        if len(k) > 0:
                            all_li.append(k)
            # 去重后所有的词
            all_pure_li = list(set(all_li))
            # print(all_str_li)
            # print(all_pure_li)
            di = dict()
            # print(len(all_pure_li))
            for ind, v in enumerate(all_pure_li):
                # print(ind + 1, v)
                di[v] = ind + 1
            f2.write(str(di))


if __name__ == '__main__':
    create_data()
