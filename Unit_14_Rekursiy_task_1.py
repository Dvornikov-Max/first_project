#Задание 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list(lst, idx=0):
    if idx < len(lst):
        print(lst[idx])
        print_list(lst, idx+1)
    else:
        print("Конец списка")

print_list(my_list)