'''
Created on 2013-3-8

@author: Administrator
'''
from scrapy import log
from scrapy.http.request import Request
from scrapy.lottery.permutation5.item import Permutation5Item
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

class Permutation5_Spider(BaseSpider):
    name = "lottery"
    url = "http://www.16788.cn/pl5/"
    start_urls = [
        "http://www.16788.cn/pl5/pl5lshaoma.asp?page=0",
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
            
            item = Permutation5Item()
            declaredate = declare_date_tag.select('text()').extract()[0].strip()
            item['declaredate'] = declaredate
            
            lottery_num = num_tag.select('strong/text()').extract()[0].strip()
            
            item['num'] = lottery_num
            
            yield item

        else:
            if tr_tags:
                log.msg("%s fetch %d row data " % (response.request._url 
                        , len(tr_tags)))
                
            next_page_xpath = '//table[@class="page"]//td[@align="center"]/a[3]/@href'
            page_a_tag = hxs.select(next_page_xpath)
            next_page_url = page_a_tag.extract()[0]
            next_page_url = self.url + next_page_url.replace(u"..", '')

            if not response.request._url == next_page_url:
                yield Request(next_page_url, self.parse)
            else:
                log.msg(u' permutation 5 from 16788 history OK . ')

