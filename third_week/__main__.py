name, age, income = [str(e) for e in input("Input: ").split()]
message = f"What is your name {name}\nWhat is your age {int(age)}\nWhat is your income {float(income):.2f}"
print(message)