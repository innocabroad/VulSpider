# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()  nsfocusItem
    nsname = scrapy.Field()       
    nsurl = scrapy.Field()        
    newdate = scrapy.Field()   
    nsupdate = scrapy.Field() 
    cvenumber = scrapy.Field() 
    nsimpact = scrapy.Field()    
    nsdatails = scrapy.Field()   

    
