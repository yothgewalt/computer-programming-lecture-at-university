def main():
    student_grade: str = ""
    student_score = int(input("\nEnter your test score: "))

    if student_score >= 90:
        student_grade = "A"
    elif student_score >= 80:
        student_grade = "B"
    elif student_score >= 70:
        student_grade = "C"
    elif student_score >= 60:
        student_grade = "D"
    else:
        student_grade = "F"

    print("Your grade is %s\n" % student_grade)

if __name__ == "__main__":
    main()