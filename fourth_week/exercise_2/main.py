gross_pay: float = 0

if __name__ == "__main__":
    worked_hour = float(input("Enter the number of hours worked: "))
    pay_rate = float(input("Enter the hourly pay rate: "))

    if worked_hour > 40:
        gross_pay = ((40 * pay_rate) + ((pay_rate * 1.5) * (worked_hour - 40)))
    else:
        gross_pay = (worked_hour * pay_rate)

    print("The gross pay is ${:,.2f}.".format(gross_pay))