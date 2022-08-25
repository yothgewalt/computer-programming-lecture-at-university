def get_name():
    first = input("Entet your first name: ")
    last = input("Enter your last name: ")

    return first, last

first_name, last_name = get_name()
print("First name:", first_name, "Last name: ", last_name)