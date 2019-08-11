import HomeWork3_def as A
"""
MAIN module
Демонстрационная программа создаёт:
- обекты класса "море"
- обекты класса "остров", связанные с классом "море"
- обекты класса "континент", связанные с классом "море"
- обекты класса "государство", связанные с классом "остров" и классом "континент"
и формирует:
- список островных государств
- список континентальных государств
- список государств, которые могут выйти к морям наземным транспортом
"""
# создать список объектов seas - моря
seas = [
    A.Sea("Северное"),
    A.Sea("Ирландское"),
    A.Sea("Атлантический"),
    A.Sea("Норвежское"),
    A.Sea("Баренцево"),
    A.Sea("Охотское"),
    A.Sea("Японское")
]


# создать список объектов isles - острова
isles = [
    A.Isle("Великобритания"),
    A.Isle("Сахалин")
]

# создать список объектов continents - континенты
continents = [
    A.Continent("Евразия")
]

# создать список объектов states - государства
states = [
    A.State("Англия"),
    A.State("Шотландия"),
    A.State("Ирландия"),
    A.State("Россия"),
    A.State("Германия"),
    A.State("Беларусь")
]

# установить для острова.континента  - какие моря омывают
isles[0].set_board_seas("Северное")
isles[0].set_board_seas("Ирландское")
isles[0].set_board_seas("Атлантический")
isles[1].set_board_seas("Охотское")
isles[1].set_board_seas("Японское")
continents[0].set_board_seas("Норвежское")
continents[0].set_board_seas("Баренцево")
continents[0].set_board_seas("Черное")

# устаеовить на каких территориях расположено государство
states[0].set_terr_span("Великобритания")
states[1].set_terr_span("Великобритания")
states[2].set_terr_span("Великобритания")
states[3].set_terr_span("Евразия")
states[3].set_terr_span("Сахалин")
states[4].set_terr_span("Евразия")
states[5].set_terr_span("Евразия")

print("Список островных государств:")
print("===========================")
for i in range(len(isles)):
    print(isles[i].type_land() + " " + isles[i].get_name())
    print("---------------------------")
    k = 0
    for j in range(len(states)):
        if isles[i].get_name() in states[j].list_terr_span():
            k +=1
            print(str(k) + ". " + states[j].get_name())

print("\n" + "Список континентальных государств:")
print("=================================")
for i in range(len(continents)):
    print(continents[i].type_land() + " " + continents[i].get_name())
    print("---------------------------------")
    k = 0
    for j in range(len(states)):
        if continents[i].get_name() in states[j].list_terr_span():
            k +=1
            print(str(k) + ". " + states[j].get_name())

print("\n" + "Список государств, которые могут выйти к морям наземным транспортом:")
print("(имеют собственный порт или граничат с государством, которое имеет порт)")
print("==================================================================")
for i in range(len(seas)):
    print("Море " + seas[i].get_name())
    print("-------------------")
    l = 0
    for j in range(len(isles)):
        if seas[i].get_name() in isles[j].list_board_seas():
            for k in range(len(states)):
                if isles[j].get_name() in states[k].list_terr_span():
                    l +=1
                    print(str(l) + ". " + states[k].get_name())
    for j in range(len(continents)):
        if seas[i].get_name() in continents[j].list_board_seas():
            for k in range(len(states)):
                if continents[j].get_name() in states[k].list_terr_span():
                    l +=1
                    print(str(l) + ". " + states[k].get_name())

