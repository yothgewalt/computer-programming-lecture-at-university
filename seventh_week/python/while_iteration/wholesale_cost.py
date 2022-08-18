def main():
    adding = "y"

    while adding == "y":
        wholesale_cost = float(input("Enter the item's wholesale cost: "))
        retail_price = wholesale_cost * 2.5

        print("Retail price: ${:,.2f}.".format(retail_price ))

        adding = input("Do you want another item? (Enter y for yes):  ")

if __name__ == "__main__": 
    main()