"""
    封装设计思想
        分而治之
        变则疏之
"""
# 需求:老张开车去东北
# 变化:老张  老李  老王  -数据不同->  使用对象区分
#     车   飞机   轮船  -行为不同->  使用类区分


# 写法1:直接创建对象调用
# 语义:老张每次使用新车去某地
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def go_to(self,position):
#         print(self.name + "去"+position)
#         car = Car()# 创建新车
#         car.run()
#
# class Car:
#     def run(self):
#         print("汽车在行驶")
#
# lz = Person("老张")
# ll = Person("老李")
# lw = Person("老王")
#
# lz.go_to("东北")
# lz.go_to("北京")


# 写法2:在构造函数中创建对象
# 语义:老张每次开自己的车去某地
# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.car = Car()  # 人的车
#
#     def go_to(self,position):
#         print(self.name + "去"+position)
#         self.car.run()
#
# class Car:
#     def run(self):
#         print("汽车在行驶")
#
# lz = Person("老张")
#
# lz.go_to("东北")
# lz.go_to("北京")

# 写法3:对象通过参数传递
# 语义:老张使用参数去某地
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,position,car):
        print(self.name + "去"+position)
        car.run()

class Car:
    def run(self):
        print("汽车在行驶")

lz = Person("老张")
car = Car()
lz.go_to("东北",car)
