# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
#from lxml import etree


class DangdangshuSpider(scrapy.Spider):
    name = 'dangdangshu'
    allowed_domains = ['dangdang.com']
    b = []
    for j in range(1,100):
        a = ['http://bang.dangdang.com/books/bestsellers/01.54.00.00.00.00-24hours-0-0-1-%s'%j]
        b = b + a
    start_urls = b
    def parse(self, response):
        li_list = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]')
        #print(li_list)
        items = []
        for li in li_list:
            item = DangdangItem()
            item['name'] = li.xpath('.//li/div[@class="name"]/a/text()').extract()
            item['title'] = li.xpath('./li/div[@class="publisher_info"]/a/@title').extract()
            item['time'] = li.xpath('./li/div[@class="publisher_info"]/span/text()').extract()
            item['price'] = li.xpath('./li/div[@class="price"]/p/span[@class="price_n"]/text()').extract()
            #item['name'] = li.xpath('./ul[@class="bang_list clearfix bang_list_mode"]/li/div[@class="name"]/a/text()').extract()
            #item['name'] = li.xpath('./ul[@class="bang_list clearfix bang_list_mode"]/li/div[@class="name"]/a/text()').extract()

            items.append(item)
        return items


