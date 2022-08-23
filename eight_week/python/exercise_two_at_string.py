def string_check():
    string_input = str(input("Enter a string: "))
    print("This is what I found about that string:")

    if string_input.isalnum():
        print("The string is alphanumeric.")

    if string_input.isalpha():
        print("The string contains only alphabetic characters.")

    if string_input.islower():
        print("The letters in the string are all lowercase.")
    elif string_input.isupper():
        print("The letters in the string are all uppercase.")
    
    if string_input.isnumeric():
        print("The string contains only digits.")

if __name__ == "__main__":
    string_check()