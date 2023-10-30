import os

path = "C:\\Users\\Killcan\\Desktop\\Text.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):    # проверка файл ли
        print("That is a file")
    elif os.path.isdir(path):   # проверка папка ли
        print("That is a directory")
else:
    print("That location doesn't exist")
