#Вводятся целые числа A и B. Гарантируется, что A ≤ B. 
# Выведите все четные числа на заданном отрезке через пробел.
A = int(input())
B = int(input())
if A > B:
    print("Ошибка. Введено А > B")
else: 
    for num in range(A, B+1):
        if num % 2 == 0:
            print(num, end=' ')