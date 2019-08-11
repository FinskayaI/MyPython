from datetime import date
# import datetime
"""
Домашняя работа 3, задание 2
Вариант 13
Создать класс "Bus"
вывести:
- список автобусов для заданного номера маршрута
- список автобусов, которые эксплуатируются больше заданного срока
"""

class Bus:
    # номер автобуса, марка, год начала эксплуатации, пробег, водитель, номер маршрута
    __bus_num = ""
    __bus_marka = ""
    __year = ""
    __kmage = 0
    __driver = ""
    __num_route = ""

    # конструктор с присвоением заданных значений
    # номер автобуса, марка, год начала эксплуатации, пробег, водитель, номер маршрута
    def __init__(self, bus_num, bus_marka, year, kmage, driver, num_route):
        self.__bus_num = bus_num
        self.__bus_marka = bus_marka
        self.__year = year
        self.__kmage = kmage
        self.__driver = driver
        self.__num_route = num_route

    # чтение марки автобуса
    def get_bus_marka(self):
        return self.__bus_marka

    # чтение номера автобуса
    def get_bus_num(self):
        return self.__bus_num

    # чтение года начала эксплуатации автобуса
    def get_bus_year(self):
        return self.__year

    # чтение пробега автобуса
    def get_bus_kmage(self):
        return self.__kmage

    # чтение имени водителя
    def get_driver(self):
        return self.__driver

    # чтение номера маршрута
    def get_num_route(self):
        return self.__num_route

    # получить возраст автобуса
    def bus_age(self):
        today = date.today()
        return today.year - self.__year

    # увеличить пробег
    def add_kmage(self, value):
        print("Автобус " + self.get_bus_num() + " увеличен пробег на : " + str(value))
        self.__kmage = self.__kmage + value

    # изменить маршрут
    def change_num_route(self, new_route):
        print("Автобус " + self.get_bus_num() + " изменён маршрут: предыдущий- " +
              self.get_num_route(), ", новый- " + new_route)
        self.__num_route = new_route

    # изменить водителя
    def change_driver(self, new_driver):
        print("Автобус " + self.get_bus_num() + " изменён водитель: предыдущий- " +
              self.get_driver(), ", новый- " + new_driver)
        self.__driver = new_driver

    # наператать информацию об автобусе
    def bus_details(self):
        print(self.get_bus_num() + "    " +
              self.get_bus_marka() + "    " +
              str(self.get_bus_year()) + "(" +
              str(self.bus_age()) + ")   " +
              str(self.get_bus_kmage()) + "    " +
              self.get_driver() + "    " +
              self.get_num_route()
              )



# main program
# создать список объектов класса "автобус"
buses = [
    Bus("AP 6414", "Mersedes", 2005, 22000, "Иванов И.И.", "15A"),
    Bus("AP 6514", "Mersedes", 2013, 42000, "Федоров И.И.", "22"),
    Bus("AP 6414", "Mersedes", 2015, 26000, "Иванов И.И.", "22"),
    Bus("AN 1218", "Mersedes", 2000, 68000, "Петров С.И.", "18"),
    Bus("KN 6414", "МАЗ", 2015, 8000, "Сидоров В.В.", "18"),
    Bus("KN 5555", "МАЗ", 1995, 128000, "Кузнецов А.Л.", "14")
]
buses[4].change_num_route("22")
buses[3].change_driver("Егоров В.Л.")
buses[3].add_kmage(12000)
print("Список всех автобусов:")
print("Номер   Марка   Год выпуска(возраст автобуса)  Пробег   Водитель    Номер маршрута ")
for i in range(len(buses)):
    buses[i].bus_details()

n = input("Введите номер маршрута:\n")
list_routes = []
for i in range(len(buses)):
    list_routes.append(buses[i].get_num_route())
while True:
    if n in list_routes:
        break
    else:
        n = input("Неправильно введён номер маршрута(нет таких в базе). Пытайтесь ввести снова:\n")

print("Список автобусов по маршруту " + n +" :")
print("Номер   Марка   Год выпуска(возраст автобуса)  Пробег   Водитель    Номер маршрута ")
for i in range(len(buses)):
    if buses[i].get_num_route() == n:
        buses[i].bus_details()

n = int(input("Введите возвраст автобуса: \n"))
print("Список всех автобусов, которые эксплуатируются больше " + str(n) + " лет:")
print("Номер   Марка   Год выпуска(возраст автобуса)  Пробег   Водитель    Номер маршрута ")
k = 0
for i in range(len(buses)):
    if buses[i].bus_age() >= n:
        buses[i].bus_details()
        k +=1
if k == 0:
    print("Таких старых автобусов в базе нет!")


