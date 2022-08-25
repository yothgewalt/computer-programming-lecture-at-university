def main():
    for x in range(5):
        _ = x # empty assign 
        print("Hello, World!")

    print("Range start, end")
    for num in range(1, 5):
        print(num)

    print("Range start, end, step")
    for num in range(1, 10, 2):
        print(num)

if __name__ == "__main__":
    main()