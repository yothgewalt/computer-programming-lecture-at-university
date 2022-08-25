def reverse_name(firstname, lastname):
    print(lastname, firstname)

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Your name reversed is")
    reverse_name(first_name, last_name)

if __name__ == "__main__":
    main()