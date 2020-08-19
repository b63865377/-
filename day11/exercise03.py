"""
    只写属性练习:
    限制鼠标实例变量在有效范围内
        品牌、      单价、   重量、    颜色
        字符小于6  0-10000、100-1000
"""


class Mouse:
    def __init__(self, brand, price, weight, colour):
        self.brand = brand
        self.price = price
        self.weight = weight
        self.colour = colour

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if len(value) < 6:
            self.__brand = value
        else:
            raise Exception("品牌字符长度过大")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if 0 <= value <= 10000:
            self.__price = value
        else:
            raise Exception("价格超狗范围")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 100 <= value <=1000:
            self.__weight = value
        else:
            raise Exception("重量不在范围内")


m01 = Mouse("双飞燕", 100, 150, "白色")
print(m01.brand)
print(m01.price)
print(m01.weight)
print(m01.colour)
