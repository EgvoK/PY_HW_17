#### TASK 01 ####
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список
# (тип списка нужно выбрать в зависимости от поставленной ниже задачи).
# После чего нужно показать меню, в котором предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение
# пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения).
# В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.

# 5,12,as,10,11,1,0,6,655,dasd,21,3,0,0,1,423,7567
from task_01_log_func import *


numbersList = []
separator = "-" * 100
numbersSet = input("Enter the set of numbers: ")
number = ""
for i in numbersSet:
    if i.isdigit():
        number = number + i
    else:
        if number != "":
            numbersList.append(int(number))
            number = ""
if number != "":
    numbersList.append(int(number))
print(numbersList)

while True:
    print(separator)
    select = input("1 - Add new number in list;\n2 - Delete number from list;\n3 - Show list;"
                   "\n4 - Show reversed list\n5 - Find number in list;\n6 - Replace number in list;"
                   "\n0 - Exit.\nEnter the action number: ")

    if select == "0":
        print(separator)
        print("Exit...")
        break

    elif select == "1":
        print(separator)
        addNumbers(numbersList)

    elif select == "2":
        print(separator)
        deleteNumbers(numbersList)

    elif select == "3":
        print(separator)
        showNumbers(numbersList)

    elif select == "4":
        print(separator)
        showReversedNumbers(numbersList)

    elif select == "5":
        print(separator)
        findNumbers(numbersList)

    elif select == "6":
        print(separator)
        replaceNumbers(numbersList)

    else:
        print(separator)
        print("Incorrect action!")
