"""
    对象计数器
        统计一个类型创建过多少对象
        要求:通过类变量实现
             画出内存图
"""

# 一个类
class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("我取了%d个老婆" % cls.count)

    # 每次创建对象都会执行构造函数
    # 所以统计对象个数,就是记录构造函数执行次数
    def __init__(self, name):
        self.name = name
        Wife.count += 1

# 五个对象
w01 = Wife("建宁")
w02 = Wife("双儿")
w03 = Wife("阿柯")
w04 = Wife("翠花")
w05 = Wife("小郡主")
Wife.print_count()
