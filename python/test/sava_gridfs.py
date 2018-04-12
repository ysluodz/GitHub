#coding=utf-8
from pymongo import MongoClient  
from bson.objectid import ObjectId  
from gridfs import *  
def insertFile():  
    client = MongoClient('localhost', 27017)  
    db = client.mydb
    fs = GridFS(db, 'images')  
    with open('F:/test/springboot.pdf'.decode('utf-8'), 'rb') as myimage:
        data=myimage.read()          
        id = fs.put(data, filename='second')
        print id

def getFile():  
    client = MongoClient('localhost', 27017)  
    db = client.mydb
    fs = GridFS(db, 'images')  
    file = fs.get_version('second', 0)
    data = file.read()  
    out = open('F:/test/test3.pdf'.decode('utf-8'), 'wb')
    out.write(data)  
    out.close()  
def delFile():
    client = MongoClient('localhost', 27017)  
    db = client.mydb
    fs = GridFS(db, 'images')  
    fs.delete(ObjectId('560a531b0d4eae34a4edbfdd'))  
def listName():  
    client = MongoClient('localhost', 27017)
    db = client.mydb
    fs = GridFS(db, 'images')
    print fs.list()     

# insertFile()
getFile()
listName()
