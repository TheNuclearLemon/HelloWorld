#text="Yooooooooooo\nThis is some text\n\nThere is free space above"
text="\nA new string in the file"
with open("Text.txt","a") as file: # w - write mode, позволяет редактировать файл / a - append, добавляет информацию в файл / as file - as переменная, может быть любое значение
    file.write(text)