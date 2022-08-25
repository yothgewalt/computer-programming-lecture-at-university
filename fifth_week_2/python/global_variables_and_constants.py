number = 0

def show_number():
    print("The number you entered is", number)

def main():
    global number
    number = int(input("Enter a number: "))
    show_number()

if __name__ == "__main__":
    main()