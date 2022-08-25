def discount(unit_price: int, quanity: int, discount: int) -> float:
    result_of_price = unit_price * quanity
    result_of_discount = ((result_of_price) * discount) / 100
    
    return result_of_price - result_of_discount

def product_sales():
    product_code = input("Enter a product code: ")
    unit_price = int(input("Enter the unit price of product: "))
    quanity = int(input("Enter the quanity of product: "))

    if product_code[1] == "1":
        result_of_sum = unit_price * quanity
        result_of_discount = ((result_of_sum) * 3) / 100
        result_price = result_of_sum - result_of_discount
        print("From Category 1")
        print("Get discount 3%")
        print("Result price is: ", result_price)
    elif product_code[1] == "2":
        if quanity < 3:
            result_of_sum = unit_price * quanity
            result_of_discount = ((result_of_sum) * 3) / 100
            result_price = result_of_sum - result_of_discount
            print("From Category 2")
            print("Get discount \"3%\" because you have quanity less than 3")
            print("Result price is: ", result_price)
        elif quanity >= 3:
            result_of_sum = unit_price * quanity
            result_of_discount = ((result_of_sum) * 5) / 100
            result_price = result_of_sum - result_of_discount
            print("From Category 2")
            print("Get discount \"5%\" because you have quanity more than 3")
            print("Result price is: ", result_price)
    else:
        result_price = unit_price * quanity
        print("You don't have any discount.")
        print("Result price is: ", result_price)

if __name__ == "__main__":
    product_sales()