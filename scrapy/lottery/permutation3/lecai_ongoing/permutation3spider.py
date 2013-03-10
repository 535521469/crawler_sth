'''
Created on 2013-3-8

@author: Administrator
'''
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy.http.request import Request
from scrapy.lottery.lotterycfg import host, user, passwd, db, smtppass
from scrapy.lottery.permutation3.item import Permutation3Item
from scrapy.lottery.permutationvo import Permutation3
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from zw.share.db.mysqlhelper import MySQLDBHelper
import datetime
from zw.share.email.emailutil import EmailUtil

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
            
            date_declaredate = datetime.datetime.strptime(declaredate, '%Y-%m-%d').date()
            
#            if date_declaredate != datetime.datetime.today():
            if date_declaredate != datetime.date(2013, 3, 9):
                continue
            
            item['declaredate'] = declaredate
            
            lottery_num = u"".join(num_tags.extract())
            
            item['num'] = lottery_num
            
            yield item

#        else:
#            if tr_tags:
#                
#                log.msg("%s %d till %s" % (response.request._url 
#                                , len(tr_tags) , declaredate))
#                
#                cur_date = datetime.datetime.strptime(declaredate, '%Y-%m-%d').date()
#                day_delta = datetime.timedelta(days= -1)
#                de_date = day_delta + cur_date
#                next_page_url = self.url + u"&de=" + unicode(de_date)
#                yield Request(next_page_url, self.parse)
#            else:
#                log.msg(u' permutation 3 from lecai history OK . ')

class MySQLPipeline(object):
    
    def process_item(self, item, spider):
        try:
            p3 = Permutation3.build_from_item(item)
            con = MySQLDBHelper.getconnection(host=host, user=user, passwd=passwd, db=db)
            sql = Permutation3.build_insert_prefix() + u",".join(map(Permutation3.prepared_insert_sql_value, [p3, ]))
            con.execute(sql)
            con.execute('commit')
            log.msg('persis one permutation 3 data ')
            
            EmailUtil.sendmsg([u"535521469@qq.com", u"13764256496@139.com"]
              , 'Lottery Info '
              , '{declaredate} lottery permutation3 is {num}'.format(**item)
              , smtppass=smtppass)
            
        except Exception as e:
            if e.args[0] == 1062:
                raise DropItem(u" %s has got ... " % item[u'declaredate'])
            else:
                raise e
        return item
    
    
