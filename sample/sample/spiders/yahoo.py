# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['search.yahoo.co.jp']
    start_urls = ['https://search.yahoo.co.jp/search?p=python']
    rules = [Rule(LinkExtractor(unique=True), callback='parse_item', follow=True)]


    def parse_item(self, response):
        print("depth:", response.request.meta['depth'])
        for div in response.css('li'):
            item = {}
            item["url"] = div.css("a::attr(href)").extract_first()
            item["text"] = div.css("a").extract()
            yield item
        for a in response.css('a'):
            yield scrapy.http.Request(a.css("::attr(href)").extract_first())

    def parse(self, response):
        return self.parse_item(response)
