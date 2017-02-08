# -*- coding: UTF-8 -*-
from scrapy import Request
from scrapy import Spider
from qingke.items import QingkeItem




class QingkeSpider(Spider):
    name = "qingkeIPO"
    allowed_domains = ["pedaily.cn"]
    global PAGE
    PAGE = 1
    start_urls=['http://zdb.pedaily.cn/ipolist.aspx?action=post&p=1&pagesize=20&url=/ipolist.aspx?i=%EF%BF%A5s=%EF%BF%A5y=%EF%BF%A5w=%EF%BF%A5p=']


    def parse(self, response):
        for sel in response.xpath('//dl'):
            item = QingkeItem()
            link = sel.xpath('dt[@class="view"]/a/@href').extract()[0]
            new_url = "http://zdb.pedaily.cn"+link
            yield Request(new_url,callback=self.parse_view)
        global PAGE
        if(PAGE<770):
            PAGE = PAGE+1
        p=str(PAGE)
        print p+'999991111111111111111111111111'
        url = "http://zdb.pedaily.cn/ipolist.aspx?action=post&p=" + p + "&pagesize=20&url=/ipolist.aspx?i=%EF%BF%A5s=%EF%BF%A5y=%EF%BF%A5w=%EF%BF%A5p="
        yield Request(url, callback=self.parse)


    def parse_view(self,response):

        item = QingkeItem()
        res = response.xpath('//div[@class="page-content"]/div[@class="zdb-top"]//div[@class="info"]')
        item['info']=res.xpath('h1/text()').extract()[0]
        try:
            item['name']=res.xpath('ul/li[1]/a/text()').extract()
            item['industry'] = res.xpath('ul/li[2]/a/text()').extract()
            item['investor']=res.xpath('ul/li[3]/text()').extract()[1].strip()   #处理不同网页不同方法
            item['time'] = res.xpath('ul/li[4]/text()').extract()[1].strip()
            item['amount'] = res.xpath('ul/li[5]/text()').extract()[1].strip()
            item['listing_location'] = res.xpath('ul/li[6]/a/text()').extract()
            item['count'] = res.xpath('ul/li[7]/text()').extract()[0]
            item['stock_code'] = res.xpath('ul/li[8]/text()').extract()[1].strip()
            item['VC_PE'] = res.xpath('ul/li[9]/text()').extract()[1].strip()
            # item['amount']=res.xpath('ul/li[3]/span[2]/text()').extract()[0]+res.xpath('ul/li/span[@class="m"]/text()').extract()[0]
            # item['rounds'] = res.xpath('ul/li[4]/text()').extract()[1].strip()
            # item['time']=res.xpath('ul/li[5]/text()').extract()[1].strip()
            # item['industry']=res.xpath('ul/li[6]/a/text()').extract()
            item['brief']=response.xpath('//*[@id="desc"]/p[2]/text()').extract()
        finally:
            yield item



