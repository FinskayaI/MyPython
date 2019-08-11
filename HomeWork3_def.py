# класс "море"
class Sea:
    # название - неизменно
    __name = ""

    # конструктор с присвоением заданного имени
    def __init__(self, name1):
        self.__name = name1

    # чтение имени
    def get_name(self):
        return self.__name

#  класс "суша"
class Land:
    __name = ""

    # конструктор с присвоением заданного имени
    def __init__(self, name2):
        self.__name = name2
        # суша омывается морями
        # в классе "суша" будет храниться список объектов класса "море"
        self.__board_seas = []

    # чтение имени
    def get_name(self):
        return self.__name

    # суша омывается морем
    def set_board_seas(self, new_sea):
        self.__board_seas.append(new_sea)
        # print("Море " + new_sea + " омывает " + self.get_name()  + "\n")

    # вывести список морей, которые омывают сушу
    def list_board_seas(self):
        return(self.__board_seas)

# класс "остров"
class Isle(Land):
    # отличается от класса "континент" только размером

    def type_land(self):
        return("Остров")

# класс "континент"
class Continent(Land):
    # отличается от класса "остров" только размером

    def type_land(self):
        return("Континент")

#  класс "государство"
class State:

    # конструктор с присвоением заданного имени
    def __init__(self, name3):
        self.__name = name3
        # государство располагается на территории континент/ов, остров/ов
        # в классе "государство" будет храниться список объектов
        # классов "остров" и "континент"
        self.__terr_span = []

    # чтение имени
    def get_name(self):
        return self.__name

    # определить, что государство располагается на территории острова или континента
    def set_terr_span(self, new_terr):
        self.__terr_span.append(new_terr)
        # print("Государство " + self.get_name() + " располагается на " + new_terr + "\n")

    # вывести список территорий, на которых располагается государство
    def list_terr_span(self):
        return(self.__terr_span)