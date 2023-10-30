import shutil
#copyfile() - копирует содержимое файла
#copy() - copyfile() + пермишен мод + конечная точка может быть папкой
#copy2() - copy() + метадата (информация о создании файла, данные об изменении и т.п.)
import os

shutil.copy("Text.txt","C:\\Users\\Killcan\\Desktop\\Copy.txt")
#src,dst - аргументы, src - source (что), dst - destination (куда)
#если dst заполнить именем, но файл будет помещен в проект / если задать имя файла - будет переименован