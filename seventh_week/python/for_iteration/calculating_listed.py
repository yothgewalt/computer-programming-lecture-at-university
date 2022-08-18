def main():
    numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
    sum = 0

    for val in numbers:
        sum += val
        print(sum)

    print("The sum is", sum)

if __name__ == "__main__":
    main()