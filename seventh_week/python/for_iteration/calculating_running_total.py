def main():
    max = 5
    total = 0.0

    print("This program calculates the sum of")
    print(max, "numbers you will enter.")

    for _ in range(max):
        number = int(input("Enter a number: "))
        total += number

    print("The total is", total)

if __name__ == "__main__":
    main()