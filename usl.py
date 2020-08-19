from bll import HouseManagerController


class HouseManagerView:
    """
       责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = HouseManagerController()

    # def main(self):
    #     while True:
    #         self.__display_menu()
    #         self.__select_menu()
    #
    # def __display_menu(self):
    #     print("1) 显示所有房源")
    #     print("2)   ")
    #     print("3)  ")
    #
    # def __select_menu(self):
    #     item = input("请输入选项:")
    #     if item == "1":
    #         self.__display_houses()
    #     elif item == "2":
    #         pass
    #     elif item == "3":
    #         pass
    #
    # def __display_houses(self):
    #     for house in self.__controller.list_houses:
    #         # 定义打印房源的格式....
    #         print(house.__dict__)

    def __display_room(self):
        print('按1键显示所有房源信息')
        print('按2键显示最贵的房源信息')
        print('按3键显示最小的房源信息')

    def __select_menu(self):
        item = input("请输入选项：")
        if item == '1':
            self.__showroomiofo()
        if item == '2':
            self.__find_expensive_room()
        if item == '3':
            self.__find_min_area_room()
        if item == '4':
            self.__get_house_type()

    def __showroomiofo(self):
        for item in self.__controller.list_houses:
            print(item.__dict__)

    def main(self):
        while True:
            self.__display_room()
            self.__select_menu()

    def __find_expensive_room(self):
        expensive_room = self.__controller.getexpensive()
        print(expensive_room.__dict__)

    def __find_min_area_room(self):
        min_area_room = self.__controller.get_min_area()
        print(min_area_room.__dict__)

    def __get_house_type(self):
        listhouse=self.__controller.find_house_type_number()
        print(listhouse)