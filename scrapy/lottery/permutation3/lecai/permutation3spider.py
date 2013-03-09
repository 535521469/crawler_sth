'''
Created on 2013-3-8

@author: Administrator
'''
from scrapy import log
from scrapy.http.request import Request
from scrapy.lottery.permutation3.item import Permutation3Item
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import datetime

class Permutation3_Spider(BaseSpider):
    name = "lottery"
    url = "http://www.lecai.com/lottery/draw/list/3?ds=2000-01-01"
    start_urls = [
        url,
    ]
    
    def parse(self, response):
        
        hxs = HtmlXPathSelector(response)
        
        tr_tags = hxs.select('//table[@id="draw_list"]//tr[@class]')
        
        for tr_tag in tr_tags:
            td_tags = tr_tag.select('td')
            
            
            declare_date_tag = td_tags[0]
            num_tags = td_tags[2].select('span/span/text()')
            
            item = Permutation3Item()
            declaredate = declare_date_tag.select('text()').extract()[0].strip()
            item['declaredate'] = declaredate
            
            lottery_num = u"".join(num_tags.extract())
            
            item['num'] = lottery_num
            
#            print declaredate, lottery_num
            yield item

        else:
            
            if tr_tags:
                
                log.msg("%s %d till %s" % (response.request._url 
                                , len(tr_tags) , declaredate))
                
                cur_date = datetime.datetime.strptime(declaredate, '%Y-%m-%d').date()
                day_delta = datetime.timedelta(days= -1)
                de_date = day_delta + cur_date
                next_page_url = self.url + u"&de=" + unicode(de_date)
                yield Request(next_page_url, self.parse)
            else:
                log.msg(u' permutation 3 from lecai history OK . ')

