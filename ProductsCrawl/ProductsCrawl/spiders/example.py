# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Aleonisa&page={}&keywords=leonisa&ie=UTF8&qid=1517933537'.format(i) for i in range(1,3)]

    def parse(self, response):
        pass
