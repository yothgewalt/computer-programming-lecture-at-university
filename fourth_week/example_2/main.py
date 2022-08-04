bonus = 0
comission_rate = 0
sales = int(input("Sales: "))

if __name__ == "__main__":  
    if sales > 50000:
        bonus = 500.0
        comission_rate = 0.12
        print("You met your sales quato")
    