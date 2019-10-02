# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient("mongodb://xxxx:xxxx@xxx.xx.xxx.xxx:xxxx")
db = client.skillmap
collection = db.leetcode

@app.route('/',methods=['GET','POSt'])
def home():
    result = collection.find_one({'question': '两数之和'})
    return '<h1>home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In </button></p>
    </form>
    '''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello ,admin!</h3>'
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    app.run(host='localhost', port=7777)