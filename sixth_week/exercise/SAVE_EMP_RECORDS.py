def main():
    employee_counts = int(input("How many employee records do you wan to create? "))
    
    employee_file = open("employees.txt", "w")

    for count in range(1, employee_counts + 1):
        print("Enter data for employee #", count, sep="")
        name = str(input("Name: "))
        employee_id = str(input("Employee ID: "))
        department = str(input("Department: "))

        employee_file.write(name + "\n")
        employee_file.write(employee_id + "\n")
        employee_file.write(department + "\n")

        print()

    employee_file.close()
    print("Employee records written to employees.txt.")

if __name__ == "__main__":
    main()