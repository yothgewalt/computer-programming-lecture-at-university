import random


def main():
    print("What is my magic number (1 to 100) ?")
    my_number = random.randint(0, 100)
    number_tries = 1
    your_guess = -1

    while number_tries < 7 and  my_number != your_guess:
        prompt_message = str(number_tries) + ">> "

        if number_tries == 6:
            print("Last round to guess number. (Limit: 6 Rounds)\nMy magic number is %s." % my_number)
        
        your_guess = int(input(prompt_message))

        if your_guess > my_number:
            print("--> too high.") 
        elif your_guess < my_number:
            print("--> too low.")

        number_tries += 1

    if your_guess == my_number:
        print("Yes, it's %s" % my_number)
    else:
        print("Sorry, my number is %s" % my_number)

if __name__ == "__main__":
    main()