'''
Created on 2013-3-9

@author: Administrator
'''
from os import path
from zw.share.db.mysqlhelper import MySQLDBHelper
import os
from scrapy.lottery.permutationvo import Permutation3

con = MySQLDBHelper.getconnection(host='localhost', user='root', passwd='root', db='Lottery')


with open(u'permutation3.json', 'r') as f:
    ls = f.readlines()

permutations = []
for l in ls:
    d = eval(l)
    permutations.append(Permutation3.build_from_dict(d))
sql = Permutation3.build_insert_prefix() + u",".join(map(Permutation3.prepared_insert_sql_value, permutations))

con.execute(sql)
con.execute('commit')

print u" store all data ... "


