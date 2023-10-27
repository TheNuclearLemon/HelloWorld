print('Here is main branch, DNT')
# master update

# Закрепление знаний
kol_uch=int(input("Введите кол-во учеников: ")) # получаем количество учеников

spisok = {} # создаем словарь для переменных
for x in range(0, kol_uch): # заполняем словарь данными
    spisok["Student info" + str(x)]=[str(input("Введите имя: ")),int(input(("Введите возраст: "))),str(input("Введите пол: "))]
for y in spisok.keys(): # превращаем словарь в список, создавая лист с данными
    Students_info=list(spisok.values())


# ch1=str(input("Укажите имя первого ученика: "))
# ch2=str(input("Укажите имя второго ученика: "))
# parametr=input("Укажите параметр для сравнения: ")
# if parametr == "Имя":
#     if ch1==ch2:
#         print("Имя одинаковое")
#     else:
#         print ("Имя разное")
# elif parametr == "Возраст":
#


# elif parametr == "Возраст":
#     for q in Students_info:
#         for w in range(0,3):
#             if ch1 == ch2:
#                 print("Одинаковое имя")
#             else:
#                 print("Имена разные")






# print(spisok)
# print(Students_info[0])