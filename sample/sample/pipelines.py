# -*- coding: utf-8 -*-

from scrapy.exporters import CsvItemExporter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SamplePipeline(object):
    def __init__(self):
        pass

    def open_spider(self, spider):
        print("\n====open spider\n")
        self.items = []

    def close_spider(self, spider):
        with open("test.csv","wb") as f:
            exporter = CsvItemExporter(f)
            exporter.start_exporting()
            for item in self.items:
                exporter.export_item(item)
            print("\n====close spider\n")
            print(self.items)
            exporter.finish_exporting()
        return self.items

    def process_item(self, item, spider):
        self.items.append(item)
        return
