#coding=utf-8
import bson.binary
from pymongo import MongoClient
from cStringIO import StringIO
def insertFile():
    client = MongoClient('localhost', 27017)
    # 获得一个database
    db = client.mydb
    # 获得一个collection
    table = db.image
    filename = 'F:/test/123.log'.decode('utf-8')
    with open(filename, 'rb') as myimage:
        content = StringIO(myimage.read())
        table.save(dict(
        content=bson.binary.Binary(content.getvalue()),
        filename='123.log'
      ))

def getFile():
    client = MongoClient('localhost', 27017)
    # 获得一个database
    db = client.mydb
    # 获得一个collection
    coll = db.image
    data = coll.find_one({'filename': '123.log'})
    out = open('F:/test/fromMongoDb.txt'.decode('utf-8'), 'wb')
    out.write(data['content'])
    out.close()

# insertFile()
getFile()