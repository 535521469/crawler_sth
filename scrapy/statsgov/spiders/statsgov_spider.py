# -*- coding:utf8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.statsgov.items import  StatsGovItemLoader, StatsGovItem
from scrapy.http.request import Request

class StatsgovSpider(BaseSpider):
    name = "statsgov"
    allowed_domains = ["statsgov.org"]
    start_urls = [
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20030219_67297.htm", # 2002-12-31
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20030722_93432.htm", # 2003-06-30
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20040211_140666.htm", # 2003-12-31
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20040607_402156425.htm", # 2004-03-31
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20041022_402202293.htm", # 2004-09-30
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20041022_402259937.htm", # 2004-12-31

    ]

    def parse(self, response):
        
        hxs = HtmlXPathSelector(response)
        
        title = hxs.select('//title/text()').extract()[0]
        
        with open(title, 'wb') as f:
            f.write(response.body)
        
        trs = hxs.select('//span[@class="content"]/table/tbody/tr')
        items = []
        
        for tr in trs:
            i = StatsGovItemLoader(StatsGovItem())
            code = tr.select("td[1]/p/span/text()").extract()[0]
            label = tr.select("td[2]/p/span/text()").extract()[0]
            
            i.add_value(u"label", label)
            i.add_value(u"code", code)
            
            items.append(i.load_item())
            
        return items



