def one_to_hundred():
    lines = int(input("How many lines?: "))

    for hundred in range(1, 101):
        print(hundred, end=" ")

        if hundred % 10 == 0:
            print("\n")

if __name__ == "__main__":
    one_to_hundred()