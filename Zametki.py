import subprocess
import os
import json
import datetime

def save(ID, title, massage):
    # объявляем переменные
    # title = "Заголовок"
    # massage = "Some test string"

    current_datetime=datetime.datetime.now()
    date = current_datetime.strftime("%c")

    zametka = {"ID": ID, "title": title, "massage": massage, "date": date}

    zametki = []
    zametki.append(zametka)
    zametki.append(zametka)

    # создаем словарь
    mydict = {"zametki": zametki}

    # сериализуем его в JSON-структуру, как строку
    x = json.dumps(mydict, ensure_ascii=False, indent=4)

    print(x)

    with open('zametki.json', 'w', encoding='utf-8') as f: f.write(x)
    
def read():
    with open("zametki.json", "r") as read_file:
        data = json.load(read_file)
        print(data)

subprocess.call('clear' if os.name =='posix' else 'cls', shell=True)    # Очистка консоли
save(1, "Заголовок", "Сообщение")
read()
