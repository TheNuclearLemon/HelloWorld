# def add(num1,num2):
#     sum=num1+num2
#     return sum
#
# print(add(1,2))

# def add(*args): # *args - позволяет использовать неограниченное количество аргументов, имеет тип tuple; "args" - название, можно использовать любое
#     sum=0
#     for i in args:
#         sum += i
#     return sum
#
# print((add(1,2,3,4)))

def add(*args):
    sum=0
    args=list(args) # можно изменить тапл на другой тип внутри функции, однако сами аргументы при входе в функцию = тапл
    args[1]=0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4))