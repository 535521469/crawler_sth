# -*- coding:utf8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Field, Item
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose

class XzqhdmItem(Item):
    
    label = Field()
    code = Field()
    enddate = Field()

class XzqhdmItemLoader(ItemLoader):
    
    default_output_processor = TakeFirst()
    
    label_in = MapCompose(unicode.strip)
    code_in = MapCompose(unicode.strip)
    enddate_in = MapCompose(unicode.strip)