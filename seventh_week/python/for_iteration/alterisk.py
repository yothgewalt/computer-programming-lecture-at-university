def main():
    rows = int(input("How many rows?: "))
    columns = int(input("How many columns?: "))

    for row in range(rows):
        for column in range(columns-1):
            print("* ", end="")
        print("*")

if __name__ == "__main__":
    main()