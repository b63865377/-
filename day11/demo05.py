"""
    属性原理
    1. 方法内部操作私有变量(私有变量是真实存储的数据)
    2. @property在创建属性对象,将下面方法作为参数
       再将对象的地址交给下面的方法名称关联
           属性名 =  property(读取方法)
    3. @age.setter 在调用属性对象的setter方法,将下面方法作为参数
       再将对象的地址交给下面的方法名称关联
           属性名.setter(写入方法)
"""


class Wife:
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        # 类变量 存储属性对象
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            raise Exception("我不要")

    # 创建属性对象 - 关联读取方法
    age = property(get_age)
    # 为属性对象关联写入方法
    age = age.setter(set_age)


w01 = Wife("双儿", 26)
w01.age = 28  # 会执行age(self,value)函数
print(w01.age)  # 会执行age(self)函数
