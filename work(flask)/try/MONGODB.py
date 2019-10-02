# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from pymongo import MongoClient
# client = MongoClient("mongodb://root:xxxxxxx@xxx.xx.xxx.xxx:xxxx")
# db = client.skillmap
# collection = db.leetcode
# result = collection.find_one({'question': '两数之和'})
app = Flask(__name__)
result = {'question': '两数之和', 'question_contant_raw': '给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。\n\n你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。\n\n示例:\n\n给定 nums = [2, 7, 11, 15], target = 9\n\n因为 nums[0] + nums[1] = 2 + 7 = 9\n所以返回 [0, 1]', 'question_contant': '给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。\n\n你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。\n\n示例:\n\n给定 nums = [2, 7, 11, 15], target = 9\n\n因为 nums[0] + nums[1] = 2 + 7 = 9\n所以返回 [0, 1]', 'url': 'https://leetcode-cn.com/problems/two-sum', 'difficulty': '简单', 'rate': '43.1%'}


@app.route('/',methods=['GET'])
def home():

    return '<h1>' \
           '    <body><p>question:{}</p><p>question_contant:{}</p><p><a href={}>url:{}</a></p><p>difficulty:{}</p><p>rate:{}</p></h1></body>'.format\
        (result['question'],result['question_contant'],result['url'],result['url'],result['difficulty'],result['rate'])



if __name__ == '__main__':
    app.run(host='localhost', port=7777)