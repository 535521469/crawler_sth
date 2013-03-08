# -*- coding:utf-8 -*-
'''
Created on 2013-3-6
@author: corleone
'''
from scrapy import log
from scrapy.http.request import Request
from scrapy.nbsc.spiders.tjbz_spider import Tjbz_Spider
from scrapy.nbsc.spiders.tjyqhdm.items import TjyqhdmItem, \
    MyJsonLinesItemExporter
from scrapy.selector import HtmlXPathSelector
import os

class Tjyqhdm_Provincetr_Spider(Tjbz_Spider):
    '''
    统计用区划代码和城乡划分代码
    '''
    
    name = "tjyqhdm"

    def parse(self, response):

        req_url = response.request._url
        
        year = response.request.cookies[u'year']
        
        hxs = HtmlXPathSelector(response)
        title = hxs.select("//title/text()").extract()[0].encode('gbk')
        enddate = u"".join(hxs.select("//strong/text()").extract())
        meta_content = hxs.select('//head/meta/@content').extract()[0]
        
        file_path = os.path.join(u"统计用区划代码和城乡划分代码", enddate) 
        
        if meta_content.find('text/html') > -1:
            file_suffix = "html"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        
        with open(file_path + os.sep + title + u"." + file_suffix, 'wb') as f:
            f.write(response.body)
        
        with open('crawl_info.cfg', 'a') as f:
            f.write(req_url + u'\n')
#
        log.msg(' Provincetr %s OK . ' % title)
        
        for prov in hxs.select('//tr[@class="provincetr"]//a'):
            url_path = prov.select('@href').extract()[0]
            code = url_path.split(u'.')[0]
            label = prov.select('text()').extract()[0]
            new_req_url_list = req_url.split('/')[:-1]
            new_req_url_list.append(url_path)
            new_req_url = u"/".join(new_req_url_list)

            item = TjyqhdmItem()
            item['label'] = label
            item['code'] = code
            item['pcode'] = 0
            item['c_v_type'] = 0
            
            jli_exp = MyJsonLinesItemExporter(open(file_path + u".json", 'a'),)
            jli_exp.export_item(item)
            
#            yield Request(new_req_url, Tjyqhdm_Citytr_Spider().parse 
#                          , priority=response.request.priority + 1
#                          , cookies={"code":code
#                                     , "label":unicode(label)
#                                     , "file_path":file_path
#                                     , 'year':year})
            
            
class Tjyqhdm_Citytr_Spider(Tjbz_Spider):
    '''
    统计用区划代码和城乡划分代码
    '''
    
    name = "tjyqhdm"

    def parse(self, response):

        req_url = response.request._url
        cookies = response.request.cookies
        priority = response.request.priority
        
        file_path = cookies[u"file_path"]
        
        year = req_url.split('/')[5]
        
        hxs = HtmlXPathSelector(response)
        label = cookies["label"]
        
        try:
            title = u"_".join((cookies["code"], unicode(priority), label.encode('gbk')))
        except UnicodeEncodeError :
            print cookies["code"], unicode(priority), label.encode('gbk')

        enddate = u"".join(hxs.select("//strong/text()").extract())
        meta_content = hxs.select('//head/meta/@content').extract()[0]
        
        if meta_content.find('text/html') > -1:
            file_suffix = "html"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        
        try:
            file_name = file_path.decode('gbk') + os.sep + title.decode('gbk') + u"." + file_suffix
        except IOError :
            print file_path.decode('gbk') , os.sep , title.decode('gbk') , u"." , file_suffix

        with open(file_name, 'wb') as f:
            f.write(response.body)
        
        with open('crawl_info.cfg', 'a') as f:
            f.write(req_url + u'\n')
        
        log.msg(' City %s OK . ' % title.encode('gbk'))
        
        for prov in hxs.select('//tr[@class="citytr"]'):
            code_a_tag, label_a_tag = prov.select('td').select('a')
            href = code_a_tag.select('@href').extract()[0]
            code = code_a_tag.select('text()').extract()[0]
            label = label_a_tag.select('text()').extract()[0]
            new_req_url_list = req_url.split('/')[:-1]
            new_req_url_list.append(href)
            new_req_url = u"/".join(new_req_url_list)
            yield Request(new_req_url, Tjyqhdm_Countytr_Spider().parse 
                          , priority=priority + 1
                          , cookies={"code":code.split('/')[-1].split(u'.')[0]
                                     , "label":unicode(label), "file_path":file_path})


class Tjyqhdm_Countytr_Spider(Tjbz_Spider):
    '''
    统计用区划代码和城乡划分代码
    '''
    
    name = "tjyqhdm"

    def parse(self, response):

        req_url = response.request._url
        cookies = response.request.cookies
        priority = response.request.priority
        
        file_path = cookies[u"file_path"]
        
        year = req_url.split('/')[5]
        
        hxs = HtmlXPathSelector(response)
        label = cookies["label"]
        try:
            title = u"_".join((cookies["code"], unicode(priority), label.encode('gbk')))
        except UnicodeEncodeError :
            print cookies["code"], unicode(priority), label.encode('gbk')
        enddate = u"".join(hxs.select("//strong/text()").extract())
        meta_content = hxs.select('//head/meta/@content').extract()[0]
        
        if meta_content.find('text/html') > -1:
            file_suffix = "html"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        
        try:
            file_name = file_path.decode('gbk') + os.sep + title.decode('gbk') + u"." + file_suffix
        except IOError :
            print file_path.decode('gbk') , os.sep , title.decode('gbk') , u"." , file_suffix
            
        with open(file_name, 'wb') as f:
            f.write(response.body)
        
        with open('crawl_info.cfg', 'a') as f:
            f.write(req_url + u'\n')
        
        log.msg(' City %s OK . ' % title.encode('gbk'))
        
        for prov in hxs.select('//tr[@class="countytr"]'):
            try:
                code_a_tag, label_a_tag = prov.select('td').select('a')
                href = code_a_tag.select('@href').extract()[0]
                code = code_a_tag.select('text()').extract()[0]
                label = label_a_tag.select('text()').extract()[0]
                new_req_url_list = req_url.split('/')[:-1]
                new_req_url_list.append(href)
                new_req_url = u"/".join(new_req_url_list)
                yield Request(new_req_url, Tjyqhdm_Towntr_Spider().parse 
                              , priority=priority + 1
                              , cookies={"code":code.split('/')[-1].split(u'.')[0]
                                         , "label":unicode(label), "file_path":file_path})
            except ValueError :
                code_td_tag, label_td_tag = prov.select('td')
                code = code_td_tag.select('text()').extract()[0]
                label = label_td_tag.select('text()').extract()[0]
                pcode = cookies[u"code"]
                item = TjyqhdmItem()
                item[u"label"] = label
                item[u"code"] = code
                item[u"pcode"] = pcode
                item[u"c_v_type"] = 0
                yield item
                
class Tjyqhdm_Towntr_Spider(Tjbz_Spider):
    '''
    统计用区划代码和城乡划分代码
    '''
    
    name = "tjyqhdm"

    def parse(self, response):

        req_url = response.request._url
        cookies = response.request.cookies
        priority = response.request.priority
        
        file_path = cookies[u"file_path"]
        
        year = req_url.split('/')[5]
        
        hxs = HtmlXPathSelector(response)
        label = cookies["label"]
        try:
            title = u"_".join((cookies["code"], unicode(priority), label.encode('gbk')))
        except UnicodeEncodeError :
            print cookies["code"], unicode(priority), label.encode('gbk')
            
        enddate = u"".join(hxs.select("//strong/text()").extract())
        meta_content = hxs.select('//head/meta/@content').extract()[0]
        
        if meta_content.find('text/html') > -1:
            file_suffix = "html"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        try:
            file_name = file_path.decode('gbk') + os.sep + title.decode('gbk') + u"." + file_suffix
        except IOError :
            print file_path.decode('gbk') , os.sep , title.decode('gbk') , u"." , file_suffix

        with open(file_name, 'wb') as f:
            f.write(response.body)
        
        with open('crawl_info.cfg', 'a') as f:
            f.write(req_url + u'\n')
        
        log.msg(' City %s OK . ' % title.encode('gbk'))
        
        for prov in hxs.select('//tr[@class="towntr"]'):
            code_a_tag, label_a_tag = prov.select('td').select('a')
            href = code_a_tag.select('@href').extract()[0]
            code = code_a_tag.select('text()').extract()[0]
            label = label_a_tag.select('text()').extract()[0]
            new_req_url_list = req_url.split('/')[:-1]
            new_req_url_list.append(href)
            new_req_url = u"/".join(new_req_url_list)
            yield Request(new_req_url, Tjyqhdm_Villagetr_Spider().parse 
                          , priority=priority + 1
                          , cookies={"code":code.split('/')[-1].split(u'.')[0]
                                     , "label":unicode(label), "file_path":file_path})

class Tjyqhdm_Villagetr_Spider(Tjbz_Spider):
    '''
    统计用区划代码和城乡划分代码
    '''
    
    name = "tjyqhdm"

    def parse(self, response):

        req_url = response.request._url
        cookies = response.request.cookies
        priority = response.request.priority
        
        file_path = cookies[u"file_path"]
        
        year = req_url.split('/')[5]
        
        hxs = HtmlXPathSelector(response)
        label = cookies["label"]
        
        try:
            title = u"_".join((cookies["code"], unicode(priority), label.encode('gbk')))
        except UnicodeEncodeError :
            title = "%s_%s_%s" % (cookies["code"], unicode(priority), label.encode('gbk'))
            
        enddate = u"".join(hxs.select("//strong/text()").extract())
        meta_content = hxs.select('//head/meta/@content').extract()[0]
        
        if meta_content.find('text/html') > -1:
            file_suffix = "html"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        try:
            file_name = file_path.decode('gbk') + os.sep + title.decode('gbk') + u"." + file_suffix
        except IOError :
            print file_path.decode('gbk') , os.sep , title.decode('gbk') , u"." , file_suffix
        except UnicodeDecodeError:
            file_name = "%s%s%s.%s" % file_path.decode('gbk') , os.sep , title.decode('gbk') , u"." , file_suffix
            print file_path.decode('gbk') , os.sep , title.decode('gbk') , u"." , file_suffix
            
        try:
            with open(file_name, 'wb') as f:
                pass
        except IOError:
            print file_name
        
        
        with open(file_name, 'wb') as f:
            f.write(response.body)
        
        with open('crawl_info.cfg', 'a') as f:
            f.write(req_url + u'\n')
        
        log.msg(' Village %s OK . ' % title.encode('gbk'))
        
#        for prov in hxs.select('//tr[@class="towntr"]//a'):
#            href = prov.select('@href').extract()[0]
#            code = prov.select('@href').extract()[0]
#            label = prov.select('text()').extract()[1]
#            new_req_url_list = req_url.split('/')[:-1]
#            new_req_url_list.append(href)
#            new_req_url = u"/".join(new_req_url_list)
            

        
        

