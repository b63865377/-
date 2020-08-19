# 定义函数,在手机列表中查找所有白色的手机
# 定义函数,在手机列表中查找品牌是"华为2"的手机对象(如果有多个返回第一个)
# 定义函数,在手机列表中查找单价小于6000的所有手机

class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

# 1
list_phones = [
    Phone("华为1", 5999, "蓝色"),
    Phone("华为2", 6999, "红色"),
    Phone("苹果1", 9999, "金色"),
    Phone("苹果2", 7999, "白色"),
    Phone("三星2", 4999, "白色"),
]


# 1)定义函数,在手机列表中查找所有白色的手机
def find_all_white():
    white_phone_list = []
    for phone in list_phones:
        if phone.color == "白色":
            white_phone_list.append(phone)
    return white_phone_list


# 2)定义函数,在手机列表中查找品牌是"华为2"的手机对象(如果有多个返回第一个)
def find_huawei2():
    for phone in list_phones:
        if phone.brand == "华为2":
            return phone


# 定义函数,在手机列表中查找单价小于6000的所有手机
def find_price_lt_6000():
    for phone in list_phones:
        if phone.price < 6000:
            return phone


# 测试
result = find_all_white()
for item in result:
    print(item.__dict__)
