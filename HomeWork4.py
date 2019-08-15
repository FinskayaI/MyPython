import os
# Домашнее задание 3
# Вариант 13

# Открыть и прочитать файл F1.txt
# прочитать как список строк
F1_filedesc = open("F1.txt", mode="r", encoding="utf-8")
print("Содержимое файла F1.txt:")
print("-----------------------")
print(F1_filedesc.read())
print("-----------------------")
# указатель на первую строку
F1_filedesc.seek(0)
F2_filedesc = open("F2.txt", mode="w", encoding="utf-8")
filecontent = F1_filedesc.readlines()
max_vowels = 0
str_no = 0
words_no = 0
list_vowels = ['А','а','О','о','И','и','Е','е','Ё','ё','Э','э','Ы','ы','У','у','Ю','ю','Я','я']

for i in range(len(filecontent)):
    # создать список слов в строке
    words = filecontent[i].split()
    if len(words) > 2:
        # запись в новый файл F2.txt
        F2_filedesc.write(filecontent[i])
    # найти слово с максимальным количеством гдасных
    # в случае более чем двух слов с одинаковым количеством гласных
    # выбирается последнее вхождение
    for j in range(len(words)):
        s = list(words[j])
        l = len([1 for x in list(words[j]) if x in list_vowels])

        if max_vowels <= l:
            max_vowels = l
            words_no = j + 1
            str_no = i + 1
            word_vowels = words[j]

print("Слово с максимальным количеством гласных (" + str(max_vowels) +
      ") - последнее вхождение: "+ word_vowels)
print("Номер строки: " + str(str_no) + " Номер слова: " + str(words_no))

F1_filedesc.close()
F2_filedesc.close()
F2_filedesc = open("F2.txt", mode="r", encoding="utf-8")
print("Содержимое файла F2.txt:")
print("-----------------------")
print(F2_filedesc.read())
F2_filedesc.close()

