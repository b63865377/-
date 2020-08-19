"""
    改造下列代码,完成只读属性
"""
import random


class Commodity:
    __start_cid = 1000

    def __init__(self, name):
        self.__cid = Commodity.__start_cid + 1
        self.__name = name
        self.__price = random.randint(10, 500)
        Commodity.__start_cid += 1

    @property
    def cid(self):
        return self.__cid

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


c01 = Commodity("商品1")
print(c01.cid)
print(c01.name)
print(c01.price)
