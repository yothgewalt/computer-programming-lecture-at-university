def price_check():
    name = input("Enter your name: ")
    message_of_photo_types = """
    Types of Photo
    1. One inch
    2. Two inch
    3. Polaroid
    """
    print(message_of_photo_types)
    photo_type = int(input("Select type: "))
    name_of_photo_type = ""
    if photo_type == 1:
        name_of_photo_type = "One inch"
    elif photo_type == 2:
        name_of_photo_type = "Two inch"
    elif photo_type == 3:
        name_of_photo_type = "Polaroid"
    else:
        print("Please try again!")

    photo_amount = int(input("Enter amount: "))

    print("Show Details")
    print("Your name is", name)
    print("Type of photo is", name_of_photo_type)
    print("Amount is", photo_amount)

    price = 0
    if photo_type == 1:
        price = 65
    elif photo_type == 2:
        price = 80
    elif photo_type == 3:
        price = 70

    net_price = 0

    if ((photo_type == 1) or (photo_type == 2)) and photo_amount >= 3:
        sum = price * photo_amount
        discount = ((sum) * 5) / 100
        print("Total price is {}*{} = {}".format(price, photo_amount, price*photo_amount))
        print("Discount =", discount)

        net_price = sum - discount
        print("Net price =", net_price)
    elif photo_type == 3:
        print("Total price is {}*{} = {}".format(price, photo_amount, price*photo_amount))
        net_price = price * photo_amount
        print("Net price =", net_price)
    else:
        print("Total price is {}*{} = {}".format(price, photo_amount, price*photo_amount))
        net_price = price * photo_amount
        print("Net price =", net_price)

if __name__ == "__main__":
    price_check()