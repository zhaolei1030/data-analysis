from pymongo import MongoClient
client = MongoClient('xxx.xxx.x.xxx', xxxxx)
db = client.lagou
collections = db.python
python_list=collections.find_one()
print(python_list)

