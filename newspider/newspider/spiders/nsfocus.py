# -*- coding: utf-8 -*-
import scrapy
from newspider.items import NewspiderItem
from scrapy.http import Request
import time,random

class NsfocusSpider(scrapy.Spider):
    name = 'nsfocus'
    allowed_domains = ['www.nsfocus.net']
    start_urls = [
        'http://www.nsfocus.net/vulndb/39001',
    ]
    def start_Requests(self):
        ua = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Connection':'keep-alive'}
        yield Request('http://www.nsfocus.net/vulndb/38999',headers=ua)
    def parse(self, response):
        nsfocusitem = NewspiderItem()
        nsfocusitem['nsname'] = response.xpath('//div[@align="center"]/b/text()').extract()
        nsfocusitem['nsurl'] = response.url
        nsfocusitem['newdate'] = response.xpath('//div[@class="vulbar"]/text()[2]').extract()
        nsfocusitem['nsupdate'] = response.xpath('//div[@class="vulbar"]/text()[3]').extract()
        nsfocusitem['cvenumber'] = response.xpath('//div[@class="vulbar"]/a[2]/text()').extract()
        nsfocusitem['nsimpact'] = response.xpath('//blockquote/text()').extract()
        nsfocusitem['nsdatails'] = response.xpath('//div[@class="vulbar"]/text()[9]').extract()
        yield nsfocusitem
        for i in range(39000,39108):
            url = "http://www.nsfocus.net/vulndb/"+str(i)
            sj = random.randint(1,5)
            time.sleep(sj)   #设置时间间隔，避免造成服务器过多压力
            yield Request(url,callback=self.parse)   #回调函数
