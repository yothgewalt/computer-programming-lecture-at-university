def main():
    print("Number\tSquare")
    print("--------------")

    for number in range(1, 11):
        square = number **2
        print(number, "\t", square)

if __name__ == "__main__":
    main()