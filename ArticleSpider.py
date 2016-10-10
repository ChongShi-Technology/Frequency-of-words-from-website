# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""
__author__="tina"
__mtime__ = '2016/10/9  10:39'
"""
import scrapy
from scrapy.selector import Selector

class ArtileSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["https://www.aint-bad.com"]
    start_urls = (
        'https://www.aint-bad.com/category/article/',
    )

    def parse(self, response):
        sel = Selector(response)
        link = 'https://www.aint-bad.com/article/page/'
        print sel
        for index in xrange(50):
            yield scrapy.Request(link+str(index+1), callback=self.parseSubclass)


    def parseSubclass(self, response):

        sel = Selector(response)
        subClass = sel.xpath('//article/header/h2/a')
        for sub in subClass:
            name = sub.xpath('text()').extract()[0]
            link = sub.xpath('@href').extract()[0]
            print name,link
            yield scrapy.Request(link, callback=self.parseContent,meta={'name':name})

    def parseContent(self, response):
        filename = response.meta['name']
        print filename
        fileClass = open('content'+filename+".txt",'w')
        content = ''
        sel = Selector(response)
        detai = sel.xpath('//*[@class="entry-content"]/p//text()').extract()
        for con in detai:
            print con
            content += con
        print content
        fileClass.write(content)
        fileClass.flush()
        fileClass.close()



