'''
Created on 2013-3-8

@author: Administrator
'''
from scrapy import log
from scrapy.http.request import Request
from scrapy.lottery.permutation3.item import Permutation3Item
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

class Permutation3_Spider(BaseSpider):
    name = "lottery"
    url = "http://www.16788.cn"
    start_urls = [
        "http://www.16788.cn/pl3/pl3lshaoma.asp?page=0",
    ]
    
    def parse(self, response):
        
        hxs = HtmlXPathSelector(response)
        
#        print response.body
        
        tr_tags = hxs.select('//table[@class="text-center "]/tr')
        
        for tr_tag in tr_tags:
            td_tags = tr_tag.select('td')
            
            declare_no_tag = td_tags[0]
            
            if declare_no_tag.select('strong'):
                continue
            
            declare_date_tag = td_tags[1]
            num_tag = td_tags[2]
#            total_volume_tag = td_tags[3]
#            detail_tag = td_tags[4]

#            print declare_no_tag.select('text()').extract()[0].strip()
            
            item = Permutation3Item()
            declaredate = declare_date_tag.select('text()').extract()[0].strip()
            item['declaredate'] = declaredate
            
            lottery_num = num_tag.select('strong/text()').extract()[0].strip()
            
            item['num'] = lottery_num
            
            print declaredate, lottery_num
            yield item

        else:
            
            next_page_xpath = '//table[@class="page"]//td[@align="center"]/a[3]/@href'
            page_a_tag = hxs.select(next_page_xpath)
            next_page_url = page_a_tag.extract()[0]
            next_page_url = self.url + next_page_url.replace(u"..", '')
            
            if not response.request._url == next_page_url:
                yield Request(next_page_url, self.parse)
            else:
                log.msg(u' permutation 3 history OK . ')

