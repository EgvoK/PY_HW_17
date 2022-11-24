def addNumbers(numbers):
    try:
        number = int(input("Enter number to add: "))
        if number in numbers:
            print("-" * 100)
            print(f"Number {number} already in list!")
        else:
            numbers.append(number)
            print("-" * 100)
            print(f"Number {number} was successfully added to the list!")

    except Exception as e:
        print(e)


def deleteNumbers(numbers):
    try:
        number = int(input("Enter number to delete: "))
        if number in numbers:
            for i in range(len(numbers) - 1, -1, -1):
                if numbers[i] == number:
                    numbers.pop(i)
            print("-" * 100)
            print(f"All numbers {number} was successfully deleted from the list!")
        else:
            print("-" * 100)
            print(f"Number {number} not found in the list!")

    except Exception as e:
        print(e)


def showNumbers(numbers):
    print(f"List: {numbers}")


def showReversedNumbers(numbers):
    print(f"Reversed list: {numbers[::-1]}")


def findNumbers(numbers):
    try:
        number = int(input("Enter number to search: "))
        if number in numbers:
            print("-" * 100)
            print(f"Number {number} is in the list!")
        else:
            print("-" * 100)
            print(f"Number {number} not found in the list!")

    except Exception as e:
        print(e)


def replaceNumbers(numbers):
    try:
        number = int(input("Enter number to replace: "))
        newNumber = int(input("Enter new number: "))
        select = input(f"1 - Replace first;\n2 - Replace all.\nEnter the action number: ")

        if number in numbers:
            if select == "1":
                for i in range(len(numbers)):
                    if numbers[i] == number:
                        numbers[i] = newNumber
                        print("-" * 100)
                        print(f"First number {number} in list was replaced to number {newNumber}!")
                        break

            elif select == "2":
                for i in range(len(numbers)):
                    if numbers[i] == number:
                        numbers[i] = newNumber
                print("-" * 100)
                print(f"Numbers {number} in list was replaced to number {newNumber}!")

            else:
                print("Incorrect action!")

        else:
            print("-" * 100)
            print(f"Number {number} not found in the list!")

    except Exception as e:
        print(e)

