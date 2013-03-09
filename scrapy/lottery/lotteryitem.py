'''
Created on 2013-3-9

@author: Administrator
'''
from scrapy.item import Field, Item

class LotteryItem(Item):
    
    declaredate = Field()
    num = Field()
