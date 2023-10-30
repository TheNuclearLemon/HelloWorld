# animal="cow"
# item="moon"
# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,"moon"))
# print("The {1} jumped over the {0}".format(item,animal,"pineapple")) #использование индексов аргументов
# print("The {animal} jumped over the {item}".format(animal="CoW",item="MooN")) #использование кейворд аргументов
#
# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# name="Name"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. There is the end of the line".format(name)) # добавляет padding - отступ (в данном случае 10 пробелов после имени
# print("Hello, my name is {:<10}. There is the end of the line".format(name)) # Hello, my name is Name      . There is the end of the line
# print("Hello, my name is {:>10}. There is the end of the line".format(name)) # Hello, my name is       Name. There is the end of the line
# print("Hello, my name is {:^10}. There is the end of the line".format(name)) # Hello, my name is    Name   . There is the end of the line
# print("Hello, my name is {name:10}. There is the end of the line".format(name="Name"))

# number=3.14159
# print("The number pi is {:.2f}".format(number)) # :.2f - формат, позволяющий показать только 2 (поэтому 2) цифры после запятой (поэтому .) в числе типа float (поэтому f)
# print("The number pi is {:.3f}".format(number)) # The number pi is 3.142
number=12345714
print("The number is {:,}".format(number)) # :, - добавляет , для разделения по тысяче (000) / The number is 10,000,000
print("The number is {:b}".format(number)) # :b - отображает число в бинарном (двоичном) виде
print("The number is {:o}".format(number)) # :o - отображает число в октальном (восьмиричном) виде
print("The number is {:x}".format(number)) # :x - отображает число в шестнадцатиричном виде (x - буквы маленькие, X - буквы большие)
print("The number is {:e}".format(number)) # :e - отображает число в научном (лол) виде (каво) (e - маленькая e, E - большая E)