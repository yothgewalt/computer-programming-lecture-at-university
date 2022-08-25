if __name__ == "__main__":
    first_score = int(input("First Score: "))
    second_score = int(input("Second Score: "))
    third_score = int(input("Third Score: "))
    average_formula = ((first_score + second_score + third_score) / 3)
    print(int(average_formula))

    if average_formula > 95:
        print("Congratulate the user")