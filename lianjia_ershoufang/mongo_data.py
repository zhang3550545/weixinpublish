#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2017/12/11 15:23
"""

import pymongo

"""
mongodb的信息封装
"""
class MongoData(object):
    # mongodb 配置信息
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    DB_NAME = 'lianjia'
    COLLECTION = 'tb_ershoufang'

    def __init__(self):
        self.client = pymongo.MongoClient(host=self.MONGO_HOST, port=self.MONGO_PORT)
        db = self.client[self.DB_NAME]
        self.collection = db[self.COLLECTION]
        print(self.collection)

    def get_collection(self):
        return self.collection

    def close(self):
        self.client.close()
