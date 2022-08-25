def student_authentication():
    firstname = str(input("Enter your firstname: "))
    lastname = str(input("Enter your lastname: "))
    student_id = str(input("Enter your student id number: "))
    
    login_as_name = firstname[:3] + lastname[:3] + student_id[-3:]

    print("Your system login name is:\n%s" % login_as_name)

if __name__ == "__main__":
    student_authentication()