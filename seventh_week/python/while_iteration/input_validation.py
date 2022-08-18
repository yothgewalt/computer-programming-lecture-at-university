def main():
    score = int(input("Enter a test score: "))
    
    while score < 0 or score > 100:
        print("ERROR: The socre cannot be negative or greater than 100.")
        score = int(input("Enter the correct score: "))

if __name__ == "__main__":
    main()