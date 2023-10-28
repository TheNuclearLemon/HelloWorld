def display_name():
    name="Name" # name - local scope, т.к. используется только внутри функции
    print(name)

second_name = "2ndname" # - global scope, переменная, доступная глобально
# внутри функции приоритет отдается локальной переменной