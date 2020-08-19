"""
    练习:
        创建敌人类
        创建实例变量并保证数据在有效范围内
            姓名、血量、攻击力
                  0-100  1 – 30
"""


# 保护数据有效范围
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("血量超过范围")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 30:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围")


e01 = Enemy("灭霸", 100, 30)
print(e01.name)
print(e01.hp)
print(e01.atk)
