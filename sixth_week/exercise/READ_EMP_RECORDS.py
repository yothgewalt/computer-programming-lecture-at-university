def main():
    employee_file = open("employees.txt", "r")
    line = employee_file.readline()

    employee_name = []
    employee_id = []
    employee_department = []

    counter = 1
    while line != "":
        line = line.strip("\n")
        
        if counter % 3 == 1:
            employee_name.append(line)

        if counter % 3 == 2:
            employee_id.append(line)

        if counter % 3 == 0:
            employee_department.append(line)

        counter += 1
        line = employee_file.readline()

    employee_file.close()

    for name, id, dept in zip(employee_name, employee_id, employee_department):
        print("Name:", name)
        print("ID:", id)
        print("Dept:", dept)

if __name__ == "__main__":
    main()