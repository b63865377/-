"""
    私有成员:只能在类中访问,类外不能访问.
        做法:以双下划线命名
        本质:障眼法
            看上去成员名称为__data,实际_MyClass__data
                  双下划线加名称     单下划线加类名加私有成员名
"""


class MyClass:
    def __init__(self):
        self.__data = 10

    def __func01(self):
        print("func01")


m01 = MyClass()
print(m01.__dict__)

# print(m01.__data) # 不能在类外访问私有变量
# m01.__func01()

# 不建议(臭流氓做法)
# m01._MyClass__data = 20
# print(m01._MyClass__data)
