#Задание 1
import math

def factorial_list(n):
    fact = math.factorial(n)
    return [math.factorial(i) for i in range(fact, 0, -1)]

number = int(input("Введите натуральное число: "))
fact = math.factorial(number)
print(f"Факториал числа {number} это {fact}")
lst = [math.factorial(i) for i in range(number, 0, -1)]
print(lst)