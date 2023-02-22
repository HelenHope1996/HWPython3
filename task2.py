# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент 
# к заданному числу X. Пользователь вводит это число с клавиатуры, список можно считать заданным.
#  Введенное число не обязательно содержится в списке.

x = int(input("Введите число:"))
list = list(map(int, input('Введите числа через пробел: ').split()))

num = 0
for i in range(len(list)):
    if list[i] < x:
        num = - num
    else:
        num = num + 0
    if list[i] >= x and list[i] - x <= num - x:
        num = list[i]
    elif list[i] <= x and num - x <= list[i] - x:
        num = list[i]
print(num)


