
import json
import datetime

# объявляем переменные
title = "Заголовок"
massage = "Some test string"

current_datetime=datetime.datetime.now()
date = current_datetime.strftime("%c")


zametka = {"ID": 1, "title": title, "massage": massage, "date": date}

zametki = []
zametki.append(zametka)
zametki.append(zametka)

# создаем словарь
mydict = {"zametki": zametki}

# сериализуем его в JSON-структуру, как строку
x = json.dumps(mydict, indent=4)

print(x)

with open('app.json', 'w', encoding='utf-8') as f: f.write(x)
    

