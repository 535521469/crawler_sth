'''
Created on 2013-3-8

@author: Administrator
'''
from scrapy.item import Field
from scrapy.lottery.lotteryitem import LotteryItem

class Permutation3Item(LotteryItem):
    
    declaredate = Field()
    num = Field()
    num1 = Field()
    num2 = Field()
    num3 = Field()
