"""
    行为封装
        创建类型时,应该保障数据在有效范围内.
        对外提供必要功能(读取年龄,修改年龄),隐藏实现细节(保护年龄范围)
    练习:exercise02
"""

# 需求:保护数据有效范围 22 ~ 30
class Wife:
    def __init__(self, name, age):
        self.name = name
        # self.age 访问的是属性property,不是实例变量
        self.age = age  # 会执行age(self,value)函数

    @property
    def age(self):# 负责读取
        return self.__age

    @age.setter
    def age(self,value):# 负责写入
        if 22 <= value <=30:
            self.__age = value
        else:
            raise Exception("我不要")


w01 = Wife("双儿", 26)
w01.age = 28  # 会执行age(self,value)函数
print(w01.age)  # 会执行age(self)函数

print(w01.__dict__)
