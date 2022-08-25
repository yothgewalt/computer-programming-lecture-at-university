def main():
    value = 99
    print("The value is", value)
    change_me(value)
    print("Back in main the value is", value)

def change_me(arg):
    print("I am changing the value.")
    arg = 0
    print("Now the value is", arg)

if __name__ == "__main__":
    main()