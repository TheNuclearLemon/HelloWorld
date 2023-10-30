import os
source="D:\\Projects\\Copy.txt"
destination="D:\\Projects\\HelloWorld\\Copy.txt"

try:
    if os.path.exists(destination):             # проверяет наличие файла, чтобы избежать перезаписи
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

# чтобы скопировать файл на другой диск - необходимо использовать shutil.move (через него делается copy, а затем delete файла)