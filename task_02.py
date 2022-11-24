#### TASK 02 ####
# Реализуйте класс стека для работы со строками (стек строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# - помещение строки в стек;
# - выталкивание строки из стека;
# - подсчет количества строк в стеке;
# - проверку пустой ли стек;
# - проверку полный ли стек;
# - очистку стека;
# - получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию.


class StringStack:
    def __init__(self):
        self.items = []
        self.length = 5

    def push(self, item):
        if len(self.items) < self.length:
            self.items.append(item)
        else:
            self.items.pop()
            self.items.append(item)

    def getQuantity(self):
        return len(self.items)

    def checkEmpty(self):
        if len(self.items) > 0:
            return "Stack is not empty"
        else:
            return "Stack is empty"

    def checkFullness(self):
        if len(self.items) == self.length:
            return "Stack is full"
        else:
            return "Stack is not full"

    def clearStack(self):
        for i in range(len(self.items)):
            self.items.pop()
        return "Stack is empty"

    def getItemValue(self, index):
        if 1 <= index <= len(self.items):
            return list(self.items)[index - 1]
        else:
            return "Error! Incorrect item number!"

    @staticmethod
    def separator():
        print("-" * 100)


newStack = StringStack()
while True:
    newStack.separator()
    select = input("1 - Add item to stack;\n2 - Get string quantity in stack;\n3 - Emptiness check;"
                   "\n4 - Fullness check;\n5 - Clear stack;\n6 - Get item value;\n0 - Exit."
                   "\nEnter action number: ")

    if select == "0":
        newStack.separator()
        print("Exit...")
        break

    elif select == "1":
        newStack.separator()
        newString = input("Enter some string: ")
        newStack.push(newString)

    elif select == "2":
        newStack.separator()
        print(f"String quantity in stack: {newStack.getQuantity()}")

    elif select == "3":
        newStack.separator()
        print(newStack.checkEmpty())

    elif select == "4":
        newStack.separator()
        print(newStack.checkFullness())

    elif select == "5":
        newStack.separator()
        print(newStack.clearStack())

    elif select == "6":
        newStack.separator()
        try:
            itemIndex = int(input(f"Enter item number: "))
            print(newStack.getItemValue(itemIndex))

        except Exception as e:
            print("Error! Incorrect item number!")

    else:
        print("Error! Incorrect action!")
