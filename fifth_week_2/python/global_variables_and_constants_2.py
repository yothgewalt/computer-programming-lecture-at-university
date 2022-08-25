import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print("Heads")
        else:
            print("Tails")

if __name__ == "__main__":
    main()