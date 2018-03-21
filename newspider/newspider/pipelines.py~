# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class NewspiderPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root',db='newspider',port=3306,charset='utf8')
        for i in range(len(item['newdate'])):
            nsname = item['nsname'][i]
            nsurl = item['nsurl']
            newdate = item['newdate'][i]
            updatetime = item['nsupdate'][i]
            cvenumber = item['cvenumber'][i]
            nsimpact = item['nsimpact'][i]
            nsdatails = item['nsdatails'][i]
            
            sql='insert into nsfocus(name,url,newdate,updatetime,cvenumber,impact,datails) values("%s","%s","%s","%s","%s","%s","%s");'%(nsname,nsurl,newdate,updatetime,cvenumber,nsimpact,nsdatails)
            try:
                conn.query(sql)
                conn.commit()
            except Exception as e:
                pass 
        conn.close()
        return item
