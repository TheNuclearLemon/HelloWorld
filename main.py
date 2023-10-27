# tuple - листы с сортировкой и неизменяемые, для группировки информации
student=("Student_name",22,"male")
print(type(student))
print(student.count("Student_name")) # сколько раз повторяется в тапле
print(student.index("male")) # какой индекс у значения

for x in student: # вывод содержимого тапла
    print(x,end=" ")
print()
if 22 in student: # проверка есть ли такое содержимое то
    print("There is 22yo guy")
