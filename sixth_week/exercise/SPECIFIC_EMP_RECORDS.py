def main():
    employee_record_file = open("employees.txt", "r")

    specific_record = input("Specific name record: ")

    employee_name = ""
    employee_id = ""
    employee_dept = ""

    reader = employee_record_file.readline()
    while reader != "":
        reader = reader.strip("\n")

        if (reader == specific_record) and (reader.isspace() == True):
            employee_name = reader
            specific_id = employee_record_file.readline()
            specific_dept = employee_record_file.readline()
            employee_id = specific_id
            employee_dept = specific_dept
            break

        reader = employee_record_file.readline()

    employee_record_file.close()

    print("Name:", employee_name)
    print("ID:", employee_id)
    print("Dept:", employee_dept)

if __name__ == "__main__":
    main()