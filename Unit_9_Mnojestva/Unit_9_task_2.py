#Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. 
# Все числа каждого списка находятся на отдельной строке. Выведите, сколько чисел содержится 
# одновременно как в первом списке, так и во втором.
list1 = set()
list2 = set()
try:
    while True:
        num = input()
        if num == '':
            break
        list1.add(int(num))
except:
    pass

try:
    while True:
        num = input()
        if num == '':
            break
        list2.add(int(num))
except:
    pass

print(len(list1 & list2))