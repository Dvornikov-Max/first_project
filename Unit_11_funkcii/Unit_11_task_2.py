#Задание 2
import collections

pets = {}

def get_pet(ID):
    return pets.get(ID, False)

def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

def pets_list():
    for ID, pet_info in pets.items():
        for name, data in pet_info.items():
            print(f"{ID}: {data['Вид питомца']} по кличке \"{name}\". Возраст питомца: {data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}. Имя владельца: {data['Имя владельца']}")

def create():
    last = max(pets.keys()) if pets else 0
    new_id = last + 1
    name = input("Имя питомца: ")
    kind = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")
    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }

def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if not pet:
        print("Питомец не найден")
    else:
        for name, data in pet.items():
            print(f"Это {data['Вид питомца']} по кличке \"{name}\". Возраст питомца: {data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}. Имя владельца: {data['Имя владельца']}")

def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(ID)
    if not pet:
        print("Питомец не найден")
    else:
        name = list(pet.keys())[0]
        kind = input("Новый вид питомца: ")
        age = int(input("Новый возраст питомца: "))
        owner = input("Новое имя владельца: ")
        pets[ID][name] = {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }

def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    if pets.pop(ID, None):
        print("Удалено")
    else:
        print("Питомец не найден")

#Цикл команд
command = ''
while command != 'stop':
    command = input("Введите команду (create/read/update/delete/list/stop): ")
    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
