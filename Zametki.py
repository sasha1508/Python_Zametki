import subprocess
import os
import json
import datetime

def add(title, massage):
    zametki = []

    readZametki = read()
    ID = CreateID(readZametki)
    for zametka in readZametki:
        tempID = zametka["ID"]
        tempTitle = zametka["title"]
        tempMassage = zametka["massage"]
        tempDate = zametka["date"]
        tempZametka = {"ID": tempID, "title": tempTitle, "massage": tempMassage, "date": tempDate}
        zametki.append(tempZametka)

    current_datetime=datetime.datetime.now()
    date = current_datetime.strftime("%c")

    zametka = {"ID": ID, "title": title, "massage": massage, "date": date}
    zametki.append(zametka)

    mydict = {"zametki": zametki}   # создаем словарь
    x = json.dumps(mydict, ensure_ascii=False, indent=4)  # сериализуем его в JSON-структуру, как строку

    #print(x)

    with open('zametki.json', 'w', encoding='utf-8') as write_file: 
        write_file.write(x)
    
def addFromID(ID, title, massage):
    zametki = []

    readZametki = read()
    for zametka in readZametki:
        tempID = zametka["ID"]
        tempTitle = zametka["title"]
        tempMassage = zametka["massage"]
        tempDate = zametka["date"]
        tempZametka = {"ID": tempID, "title": tempTitle, "massage": tempMassage, "date": tempDate}
        zametki.append(tempZametka)

    current_datetime=datetime.datetime.now()
    date = current_datetime.strftime("%c")

    zametka = {"ID": ID, "title": title, "massage": massage, "date": date}
    zametki.append(zametka)

    mydict = {"zametki": zametki}   # создаем словарь
    x = json.dumps(mydict, ensure_ascii=False, indent=4)  # сериализуем его в JSON-структуру, как строку

    with open('zametki.json', 'w', encoding='utf-8') as write_file: 
        write_file.write(x)

def read():
    with open("zametki.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data["zametki"]

def printAll():
    zametki = read()
    for zametka in zametki:
        print(str(zametka["ID"]) + " - " + str(zametka["title"]))
        print(zametka["massage"])
        print(zametka["date"])
        print("")

def printFromID(ID):
    zametki = read()
    for zametka in zametki:
        if str(zametka["ID"]) == ID:
            print(str(zametka["ID"]) + " - " + str(zametka["title"]))
            print(zametka["massage"])
            print(zametka["date"])
            print("")

def delete(ID):
    zametki = read()
    for zametka in zametki:
        if int(zametka["ID"]) == int(ID):
            zametki.remove(zametka)
    mydict = {"zametki": zametki}   # создаем словарь
    x = json.dumps(mydict, ensure_ascii=False, indent=4)  # сериализуем его в JSON-структуру, как строку
    with open('zametki.json', 'w', encoding='utf-8') as write_file: 
        write_file.write(x)

def edit(ID, title, massage):
    zametki = read()
    for zametka in zametki:
        if str(zametka["ID"]) == ID:
            tempTitle = zametka["title"]
            tempMassage = zametka["massage"]
    if title == "": title = tempTitle
    if massage == "": massage = tempMassage
    delete(ID)
    addFromID(ID, title, massage)

def CreateID(readZametki):
    ID = 0
    IDGood = False
    while IDGood == False:
        IDGood = True
        for zametka in readZametki:
            if ID == zametka["ID"]:
                ID = ID + 1
                IDGood = False
                break
    return ID  
   

while True:
    subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли
    print("Описание команд:")
    print("print - отобразить все заметки")
    print("add - добавить заметку")
    print("edit - редактировать заметку")
    print("del - удалить заметку")
    print("exit - выход из программы")

    inputString = input()
    if inputString == "exit": break
    if inputString == "print": 
        printAll()
        input()
    if inputString == "add": 
        title = input("Введите заголовок заметки: ")
        massage = input("Введите текст заметки: ")
        add(title, massage)
        input("Заметка добавлена")
    if inputString == "del": 
        ID = input("Введите ID удаляемой заметки: ")
       
        delete(ID)
        input("Заметка удалена")

    if inputString == "edit": 
        ID = input("Введите ID редактируемой заметки: ")
        while True:
            subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли
            printFromID(ID)
            title = ""
            massage = ""
            command = input("Введите команду (t - поменять заголовок, m - поменять текст заметки, x - выход из редактирования): ")
        
            if command == "t":
                title = input("Введите заголовок заметки: ")
            elif command == "m":
                massage = input("Введите текст заметки: ")
            elif command == "x": break
            edit(ID, title, massage)
            input("Сохранено ")
