# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QingkeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    info = scrapy.Field()       #信息
    investor = scrapy.Field()   #投资方
    amount = scrapy.Field()     #金额
    count = scrapy.Field()      #发行量
    time = scrapy.Field()       #注册时间  上市时间
    listing_location = scrapy.Field()   #上市地点
    stock_code = scrapy.Field() #股票代码
    industry = scrapy.Field()    #所属行业
    VC_PE = scrapy.Field()      #是否VC／PE支持
    brief = scrapy.Field()      #简介


    pass
