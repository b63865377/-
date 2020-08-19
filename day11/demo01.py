"""
    类成员
        类变量
            在类中方法外创建
                变量名 = 数据
            使用
                类名.变量名
        类方法
            创建
                @classmethod
                def 方法名(cls):
                    cls 就是 类名
            使用
                类名.方法名()
    练习:exercise01
"""


class ICBC:
    # 类变量:总行(大家)的数据
    total_money = 10000000

    # 类方法:操作类变量
    @classmethod
    def print_total_money(cls):
        # 通过类名方法类变量与通过cls访问类变量,效果相同,但后者代码可读性更高
        # print("总行的钱是%d" % ICBC.total_money)
        print("总行的钱是%d" % cls.total_money)  # 建议

    def __init__(self, name, money):
        # 实例变量:支行(自己)的数据
        # 每次创建一个支行,就会在内存中分配一套实例变量
        self.name = name
        self.money = money
        # 总行钱减少
        ICBC.total_money -= self.money


ttzh = ICBC("天坛支行", 1000000)
trtzh = ICBC("陶然亭支行", 2000000)

# 通过对象访问实例成员
print(ttzh.name)
# 通过类访问类成员
print(ICBC.total_money)

# 访问类方法使用类.
ICBC.print_total_money() # print_total_money(ICBC)