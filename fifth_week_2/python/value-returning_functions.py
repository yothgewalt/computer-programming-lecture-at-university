DISCOUNT_PERCENTAGE = 0.20

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print("The sale price is $", format(sale_price, ",.2f"), sep="")

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

if __name__ == "__main__":
    main()