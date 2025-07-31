'''
Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? 
Гласными называют буквы «a», «e», «i», «o», «u».
Для решения задачи создайте переменную и в неё положите слово с помощью input().
А также определите количество каждой из этих гласных букв. Если какой-то из перечисленных букв нет - Выведите False#
'''
word = (input("Введите слово маленькими латинскими буквами:"))
glasn = 'aeiou'
glasn_counts = {v: 0 for v in glasn}
glasn_total = 0
consonant_total = 0

for letter in word:
    if letter in glasn:
        glasn_counts[letter] += 1
        glasn_total += 1
    else:
        consonant_total += 1

print(word)
print("Гласные:", glasn_total)
print("Согласные:", consonant_total)

for v in glasn:
    result = glasn_counts[v] if glasn_counts[v] > 0 else False
    print(f"Количество {v}: {result}")
