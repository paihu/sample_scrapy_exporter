# -*- coding: utf-8 -*-
import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['search.yahoo.co.jp']
    start_urls = ['https://search.yahoo.co.jp/search?p=python']

    def parse(self, response):
        for div in response.css('li'):
            item = {}
            item["url"] = div.css("a::attr(href)").extract_first()
            item["text"] = div.css("a").extract()
            yield item

