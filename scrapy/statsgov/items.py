# -*- coding:utf8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import  MapCompose, Join, TakeFirst
from scrapy.item import Field, Item

class StatsGovItem(Item):
    
    label = Field()
    code = Field()

class StatsGovItemLoader(ItemLoader):
    
    default_output_processor = TakeFirst()
    
    label_in = MapCompose(unicode.strip)
    code_in = MapCompose(unicode.strip)
    
