"""
练习:将下列面向过程的代码改为面向对象的代码
list_employees = [
    {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
]

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]


def print_employee(emp):
    print(f"{emp['name']}的员工编号是{emp['eid']},部门编号是{emp['did']},月薪{emp['money']}元.")


# 1. 定义函数,打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employees_by_all():
    for emp in list_employees:
        print_employee(emp)


# 2. 定义函数,打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employees_by_gt_2w():
    for emp in list_employees:
        if emp['money'] > 20000:
            print_employee(emp)


# 3. 定义函数,在部门列表中查找编号最小的部门
def get_min_by_did():
    min_value = list_departments[0]
    for i in range(1, len(list_departments)):
        # 通过变量比较字典的值
        if min_value["did"] > list_departments[i]["did"]:
            # 替换变量
            min_value = list_departments[i]
    return min_value


# 4. 定义函数,根据部门编号对部门列表降序排列
def descending_order_by_did():
    for r in range(len(list_departments) - 1):
        for c in range(r + 1, len(list_departments)):
            if list_departments[r]["did"] < list_departments[c]["did"]:
                list_departments[r], list_departments[c] = list_departments[c], list_departments[r]
"""


class Employees:
    def __init__(self, eid, did, name, money):
        self.money = money
        self.name = name
        self.did = did
        self.eid = eid


class Departments:
    def __init__(self, did, title):
        self.title = title
        self.did = did


list_employees = [
    Employees(1001, 9002, '师父', 60000),
    Employees(1002, 9001, '孙悟空', 50000),
    Employees(1003, 9002, '猪八戒', 20000),
    Employees(1004, 9001, '沙僧', 30000),
    Employees(1005, 9001, '小白龙', 15000),
]

list_departments = [
    Departments(9001, '教学部'),
    Departments(9002, '销售部'),
    Departments(9003, '品保部'),
]


# 容器[键]
def print_employee(emp):
    print(f"{emp.name}的员工编号是{emp.eid},部门编号是{emp.did},月薪{emp.money}元.")


# 1. 定义函数,打印所有员工信息,
def print_employees_by_all():
    for emp in list_employees:
        print_employee(emp)


# 2. 定义函数,打印所有月薪大于2w的员工信息,
def print_employees_by_gt_2w():
    for emp in list_employees:
        if emp.money > 20000:
            print_employee(emp)


# 3. 定义函数,在部门列表中查找编号最小的部门
def get_min_by_did():
    min_value = list_departments[0]
    for i in range(1, len(list_departments)):
        if min_value.did > list_departments[i].did:
            min_value = list_departments[i]
    return min_value


# 4. 定义函数,根据部门编号对部门列表降序排列
def descending_order_by_did():
    for r in range(len(list_departments) - 1):
        for c in range(r + 1, len(list_departments)):
            if list_departments[r].did < list_departments[c].did:
                list_departments[r], list_departments[c] = list_departments[c], list_departments[r]


result = get_min_by_did()
# 打印自定义对象格式:<__main__.类名 object at 内存地址>
# print(result)
print(result.__dict__)
