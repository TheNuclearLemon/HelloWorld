# with open('File_path') - можно открыть по указанному пути, либо как ниже - если файл в проекте
try:
    with open('Text.txt') as file: # таким способом файл будет закрыт после выполнения
        print(file.read())
except FileNotFoundError:
    print("That file was not found")