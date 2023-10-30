import os
import shutil

path="empty_folder"
try:
    os.remove(path) # для удаления файлов
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You don't have permission to delete dir")
else:
    print(path+" was deleted")

# для удаления ПУСТОЙ папки используется os.rmdir(path)
os.rmdir("empty_folder")
# для удаления папки с ФАЙЛАМИ используется shutil.rmtree(path)
shutil.rmtree("folder")