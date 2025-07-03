print("Дано пятизначное целое число. Напишите алгоритм, который возведёт количество десятков в степень " \
"количества единиц. Затем умножит это число на количество сотен. И делит получившееся число на разность " \
"количества десятков тысяч и количества тысяч. Задача будет решена на примере числа 46275")
number = 46275
ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_of_thousands = (number // 10000) % 10
result = tens ** ones
result = result * hundreds
result /= (tens_of_thousands - thousands)
print(result)
