### 链家二手房分析

1. 上海链家网爬取二手房信息（见爬虫项目），数据存储于mongodb。
    
    爬虫项目链接：
    > https://github.com/zhang3550545/scrapy-spider/tree/master/lianjia

2. 从mongodb中读取数据，清洗数据，写入csv文件

    先执行mongodb_to_csv.py文件，将mongodb数据清洗后，生成csv文件。
    
3. 从csv文件中，读取需要的数据，分析，使用plot绘制相应的图表

    执行data_deal.py文件，生成需要的图标（生成图标需要打开注释）。