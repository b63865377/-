"""
    属性各种写法
        读写
        只读
        只写(最不常用)
"""

# 写法1:读写属性
# 作用:可以在读取和写入数据时进行有效性验证
# 快捷键: props + 回车
class MyClass:
    def __init__(self, data):
        self.data = data

    @property
    def data(self): # 负责读取
        return self.__data

    @data.setter
    def data(self, value):# 负责写入
        self.__data = value

m01 = MyClass(10)
print(m01.data)

"""
# 写法2:只读属性
# 作用:限制数据只能被读取,不能被修改
# 快捷键:prop + 回车
class MyClass:
    def __init__(self):
        self.__data = 10

    @property
    def data(self):
        return self.__data

m01 = MyClass()
print(m01.data)
# 不能修改
# m01.data = 20# AttributeError: can't set attribute
"""

"""
# 写法3:只写属性
# 作用:限制数据只能被修改,不能被读取
class MyClass:
    def __init__(self, data):
        self.data = data

    data = property()
    @data.setter
    def data(self, value):# 负责写入
        self.__data = value

    # def set_data(self, value):# 负责写入
    #     self.__data = value
    # data = property(None,set_data)

m01 = MyClass(10)
print(m01.data)# AttributeError: unreadable attribute
print(m01.__dict__)
"""