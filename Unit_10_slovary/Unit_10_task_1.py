#Задание 1
pets = {}
name = input("Имя питомца: ")
kind = input("Вид питомца: ")
age = int(input("Возраст питомца: "))
owner = input("Имя владельца: ")
pets[name] = {"Вид питомца": kind, "Возраст питомца": age, "Имя владельца": owner}

# Функция для определения суффикса
def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

print(f"Это {pets[name]['Вид питомца']} по кличке \"{name}\". Возраст питомца: {pets[name]['Возраст питомца']} {get_suffix(pets[name]['Возраст питомца'])}. Имя владельца: {pets[name]['Имя владельца']}")
