message = """
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide
"""

def main():
    print(message)
    select_operation = input("Select operations from 1, 2, 3, 4: ")

    if select_operation == "1" or select_operation == "2" or select_operation == "3" or select_operation == "4":
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        if select_operation == "1":
            answer = first_number + second_number
            print(f"{first_number} - {second_number} = {answer}")
        elif select_operation == "2":
            answer = first_number - second_number
            print(f"{first_number} - {second_number} = {answer}")
        elif select_operation == "3":
            answer = first_number * second_number
            print(f"{first_number} * {second_number} = {answer}")
        elif select_operation == "4":
            answer = first_number / second_number
            print(f"{first_number} / {second_number} = {answer}")
    else:
        print("Operation error")

if __name__ == "__main__":
    main()