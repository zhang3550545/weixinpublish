#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2017/12/11 15:38
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def zone_avg_price(date):
    """
    1.上海各区平均房价
    :param date:
    :return:
    """
    df2 = date.groupby(by=['zone'])['priceUnit'].mean()
    zones = np.array(df2.index)
    X = range(zones.size)
    prices = np.array(df2)
    Y = prices

    plt.figure(figsize=(10, 6))
    plt.title('2017年12月上海各区域二手房挂牌平均价格(单位/元)', fontproperties=font_text)
    plt.bar(X, Y)
    plt.xticks(X, zones, fontproperties=font_text)
    for x, y in zip(X, Y):
        plt.text(x, y + 1500, '%.1f' % y, ha='center', fontproperties=font_num)
    plt.show()


def area_avg_price(data, area):
    """
    2.上海各区域各版块的房屋挂牌均价
    :param data:
    :param area:
    :return:
    """
    df2 = data.groupby(by=['zone', 'area'])['priceUnit'].mean()
    data2 = df2.ix[[area]]
    areas = data2[area].index
    prices = np.array(data2)
    X = range(areas.size)
    Y = prices
    if area == '浦东':
        plt.figure(figsize=(20, 6))
    else:
        plt.figure(figsize=(10, 6))
    plt.title('2017年12月上海%s区各版块二手房挂牌平均价格(单位/元)' % area, fontproperties=font_text)
    plt.bar(X, Y)
    plt.xticks(X, areas, rotation=30, fontproperties=font_text)
    for x, y in zip(X, Y):
        plt.text(x, y + 1500, '%.1f' % y, ha='center', fontproperties=font_num)
    plt.show()


def zone_sum(data):
    """
    3.上海各区域挂牌房屋量
    :param data:
    :return:
    """
    results = data['zone'].value_counts()
    keys = np.array(results.index)
    values = np.array(results)
    X = range(len(keys))
    Y = values
    plt.figure(figsize=(10, 6))
    plt.title('2017年12月上海各区域二手房挂牌量', fontproperties=font_text)
    plt.bar(X, Y)
    plt.xticks(X, keys, rotation=30, fontproperties=font_text)
    for x, y in zip(X, Y):
        plt.text(x, y + 10, '%.0f' % y, ha='center', fontproperties=font_num)
    plt.show()


def area_sum(data):
    """
    4.上海各版块挂牌房屋量前20
    :param data:
    :return:
    """
    results = data['area'].value_counts()
    keys = np.array(results.index)[0:20]
    values = np.array(results)[:20]
    X = range(len(keys))
    Y = values
    plt.figure(figsize=(13, 6))
    plt.title('2017年12月上海二手房挂牌量前20版块', fontproperties=font_text)
    plt.bar(X, Y)
    plt.xticks(X, keys, rotation=30, fontproperties=font_text)
    for x, y in zip(X, Y):
        plt.text(x, y + 1, '%.0f' % y, ha='center', fontproperties=font_num)
    plt.show()


def bulid_time(data):
    """
    5.上海挂牌房屋建造时间比（-80,81-85,86-90,91-95,96-00,01-05,06-10,10-）
    :param data:
    :return:
    """
    raw = data['buildTime']
    mask = raw.notnull()
    builds = raw[mask]
    results = builds.value_counts()
    x = ['1980年前', '1980年-1984年', '1985年-1989年', '1990年-1994年', '1995年-1999年', '2000年-2004年', '2005年-2009年', '2010年后']
    y = np.zeros(len(x))
    for index in results.index:
        if index < 1980.0:
            y[0] = results[index] + y[0]
        elif index < 1985.0:
            y[1] = results[index] + y[1]
        elif index < 1990.0:
            y[2] = results[index] + y[2]
        elif index < 1995.0:
            y[3] = results[index] + y[3]
        elif index < 2000.0:
            y[4] = results[index] + y[4]
        elif index < 2005.0:
            y[5] = results[index] + y[5]
        elif index < 2010.0:
            y[6] = results[index] + y[6]
        else:
            y[7] = results[index] + y[7]

    plt.figure(figsize=(10, 6))
    plt.title('2017年12月上海二手房挂牌量房屋建造年限', fontproperties=font_text)
    labels = x
    sizes = y
    patches, l_text, s_text = plt.pie(sizes, labels=labels, labeldistance=1.05,
                                      autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.75)

    for t in l_text:
        # 设置饼状图labels中文，解决中文乱码
        t.set_fontproperties(font_text)

    # 设置x,y轴一样，呈圆形
    plt.axis('equal')
    # 设置图例prop属性，解决中文乱码
    plt.legend(prop=font_text)
    plt.show()


def house_size(data):
    """
    6.上海挂牌房屋面积占比（20以下，20-40,40-60,60-80,80-100,100-120,120-140,140以上）
    :param data:
    :return:
    """
    results = data['size'].value_counts()
    x = ['40㎡以下', '40㎡-60㎡', '60㎡-80㎡', '80㎡-100㎡', '100㎡-120㎡', '120㎡-140㎡', '140㎡-160㎡', '160㎡以上']
    y = np.zeros(len(x))
    for index in results.index:
        if index < 40.0:
            y[0] = results[index] + y[0]
        elif index < 60.0:
            y[1] = results[index] + y[1]
        elif index < 80.0:
            y[2] = results[index] + y[2]
        elif index < 100.0:
            y[3] = results[index] + y[3]
        elif index < 120.0:
            y[4] = results[index] + y[4]
        elif index < 140.0:
            y[5] = results[index] + y[5]
        elif index < 160.0:
            y[6] = results[index] + y[6]
        else:
            y[7] = results[index] + y[7]

    plt.figure(figsize=(12, 8))
    plt.title('2017年12月上海二手房挂牌量房屋面积大小分布', fontproperties=font_text)
    labels = x
    sizes = y
    patches, l_text, s_text = plt.pie(sizes, labels=labels, labeldistance=1.05,
                                      autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.75)

    for t in l_text:
        # 设置饼状图labels中文，解决中文乱码
        t.set_fontproperties(font_text)

    # 设置x,y轴一样，呈圆形
    plt.axis('equal')
    # 设置图例prop属性，解决中文乱码
    plt.legend(prop=font_text)
    plt.show()


def room_shape(data):
    """
    7.上海挂牌房屋几房几厅占比（一房一厅，两房一厅，两房两厅，三房两厅，四房两厅，...）
    :param data:
    :return:
    """
    results = data['room'].value_counts()
    x = ['1室0厅', '1室1厅', '1室2厅', '2室0厅', '2室1厅', '2室2厅', '3室1厅', '3室2厅', '4室2厅', '其他']
    y = np.zeros(len(x))
    for index in results.index:
        if index == x[0]:
            y[0] = results[index]
        elif index == x[1]:
            y[1] = results[index]
        elif index == x[2]:
            y[2] = results[index]
        elif index == x[3]:
            y[3] = results[index]
        elif index == x[4]:
            y[4] = results[index]
        elif index == x[5]:
            y[5] = results[index]
        elif index == x[6]:
            y[6] = results[index]
        elif index == x[7]:
            y[7] = results[index]
        elif index == x[8]:
            y[8] = results[index]
        else:
            y[9] = results[index] + y[9]

    plt.figure(figsize=(12, 8))
    plt.title('2017年12月上海二手房挂牌量房屋格局分布', fontproperties=font_text)
    labels = x
    sizes = y
    patches, l_text, s_text = plt.pie(sizes, labels=labels, labeldistance=1.05,
                                      autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.75)

    for t in l_text:
        # 设置饼状图labels中文，解决中文乱码
        t.set_fontproperties(font_text)

    # 设置x,y轴一样，呈圆形
    plt.axis('equal')
    # 设置图例prop属性，解决中文乱码
    plt.legend(prop=font_text)
    plt.show()


# 上海链家网二手房在售房源：3000数据
#
# 1.上海各区域的房屋挂牌均价
# 2.上海各区域各版块的房屋挂牌均价
# 3.上海各区域挂牌房屋量
# 4.上海各区域各版块的挂牌房屋量,前20
# 5.上海挂牌房屋建造时间比（81-85,86-90,91-95,96-00,01-05,06-10,10-）
# 6.上海挂牌房屋面积占比（20以下，20-40,40-60,60-80,80-100,100-120,120-140,140以上）
# 7.上海挂牌房屋几房几厅占比（一房一厅，两房一厅，两房两厅，三房两厅，四房两厅，...）

if __name__ == '__main__':
    # 从csv文件中读取数据
    data = pd.read_csv('lianjia_house.csv')
    # 字体
    font_text = FontProperties(fname='C:\Windows\Fonts\simkai.ttf', size=12)
    font_num = FontProperties(fname='C:\Windows\Fonts\simkai.ttf', size=9)

    # 1.上海各区域均价
    zone_avg_price(date=data)

    # 2.上海各区版块价格
    # area_avg_price(data, area='徐汇')
    # area_avg_price(data, area='黄浦')
    # area_avg_price(data, area='闵行')
    # area_avg_price(data, area='浦东')

    # 3.上海各区域挂牌房屋量
    # zone_sum(data)

    # 4.上海各版块挂牌房屋量前20
    # area_sum(data)

    # 5.上海挂牌房屋建造时间比（-80,81-85,86-90,91-95,96-00,01-05,06-10,10-）
    # bulid_time(data)

    # 6.上海挂牌房屋面积占比（20以下，20-40,40-60,60-80,80-100,100-120,120-140,140以上）
    # house_size(data)

    # 7.上海挂牌房屋几房几厅占比（一房一厅，两房一厅，两房两厅，三房两厅，四房两厅，...）
    # room_shape(data)
