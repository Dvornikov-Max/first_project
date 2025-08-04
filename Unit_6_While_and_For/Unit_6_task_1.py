#Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, 
# сколько из них равны нулю, и выведите это количество.
N = int(input())
count_zero = 0
for _ in range(N):
    num = int(input())
    if num == 0:
        count_zero += 1
print(count_zero)