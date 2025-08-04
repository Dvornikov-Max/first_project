#Вводится натуральное число X. Подсчитайте количество натуральных 
# делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)
X = int(input())
count_div = 0
for i in range(1, int(X**0.5)+1):
    if X % i == 0:
        count_div += 2 if i != X // i else 1
print(count_div)