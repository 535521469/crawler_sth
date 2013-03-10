'''
Created on 2013-3-10

@author: Administrator
'''

class Permutation(object):
    
    def __init__(self, declaredate, num):
        self._declaredate = declaredate
        self._num = num

class Permutation3(Permutation):
    
    def __init__(self, declaredate, num):
        super(Permutation3, self).__init__(declaredate, num)
        self._num1 = num[0]
        self._num2 = num[1]
        self._num3 = num[2]
        
    def prepared_insert_sql_value(self):
        return (u"('{self._declaredate}',{self._num1},{self._num2}"
                    ",{self._num3})").format(**locals())
    
    @staticmethod
    def build_from_dict(d, declaredate=u"declaredate", num=u"num"):
        p = Permutation3(d[declaredate], d[num])
        return p

    @staticmethod
    def build_from_item(item):
        return Permutation3.build_from_dict(item)
    
    
    @staticmethod
    def build_insert_prefix():
        return (u" insert into Lottery.Permutation3 "
                    "(DeclareDate,Num1,Num2,Num3) values ")

class Permutation5(Permutation):
    
    def __init__(self, declaredate, num):
        super(Permutation5, self).__init__(declaredate, num)
        self._num1 = num[0]
        self._num2 = num[1]
        self._num3 = num[2]
        self._num4 = num[3]
        self._num5 = num[4]
        
    def prepared_insert_sql_value(self):
        return (u"('{self._declaredate}',{self._num1},{self._num2}"
                    ",{self._num3},{self._num4},{self._num5})").format(**locals())
    
    @staticmethod
    def build_from_dict(d, declaredate=u"declaredate", num=u"num"):
        p = Permutation5(d[declaredate], d[num])
        return p
    
    @staticmethod
    def build_insert_prefix():
        return (u" insert into Lottery.Permutation5 "
                    "(DeclareDate,Num1,Num2,Num3,Num4,Num5) values ")
    
