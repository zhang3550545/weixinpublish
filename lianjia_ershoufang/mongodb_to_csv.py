#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2017/12/23 8:19
"""

from lianjia_ershoufang.mongo_data import MongoData
import pandas as pd

"""
使用pandas模块，从mongodb读取数据，写入csv文件
"""
if __name__ == '__main__':
    mongo = MongoData()
    collection = mongo.get_collection()
    df = pd.DataFrame(list(collection.find()))
    # 数据清洗
    df['buildTime'] = df['buildTime'].str.extract('(\d+)', expand=True)
    df['money'] = df['money'].str.extract('(\d+)', expand=True)
    df['priceUnit'] = df['priceUnit'].str.extract('(\d+)', expand=True)
    df['size'] = df['size'].str.replace('平', '')

    df.to_csv('lianjia_house.csv', encoding='utf-8')
