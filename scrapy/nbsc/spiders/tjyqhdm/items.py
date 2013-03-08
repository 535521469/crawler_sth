# -*- coding:utf8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Field, Item
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose
from scrapy.contrib.exporter import JsonLinesItemExporter
import json

class TjyqhdmItem(Item):
    
    label = Field()
    code = Field()
    pcode = Field()
    c_v_type = Field() # 城乡分类
    
class MyJsonLinesItemExporter(JsonLinesItemExporter):
    
    def serialize_field(self, field, name, value):
        if name == u'label':
            return value
        else:
            return JsonLinesItemExporter.serialize_field(self, field, name, value)
    
    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
#        content = self.encoder.encode(itemdict)
        content = json.dumps([itemdict, ], encoding='gbk')
        self.file.write(content + '\n')
