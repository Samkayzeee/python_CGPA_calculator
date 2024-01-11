def calculate_gpa(marks):
    if 100 >= marks >= 70:
        return 5, "A"
    elif 60 <= marks < 90:
        return 4, "B"
    elif 50 <= marks < 60:
        return 3, "C"
    elif 45 <= marks < 50:
        return 2, "D"
    elif 40 <= marks < 45:
        return 1, "C"
    elif 40 > marks >= 0:
        return 0, "F"
    else:
        return 0, "Input Normal Score"

def main():
    semesters = int(input("Enter the number of semesters: "))
    total_credits = 0
    final_gpa = []

    for semester in range(1, semesters + 1):
        print(f"Entering details for Semester {semester}")
        subjects = int(input("Enter the number of subjects: "))
        semester_gpa = 0
        total_semester_credits = 0

        for subject in range(1, subjects + 1):
            marks = int(input(f"Enter marks for Subject {subject}: "))
            credits = int(input(f"Enter credits for Subject {subject}: "))

            subject_gpa, grade = calculate_gpa(marks)
            print(f"Grade for Subject {subject}: {grade}")

            if marks > 100:
                print("You have marks greater than 100 Input score between 1 and 100.")
                return
            if marks < 0:
                print("Cannot Input negative number as a Score.")
                return

            semester_gpa += subject_gpa * credits
            total_semester_credits += credits

        semester_gpa /= total_semester_credits
        total_credits += total_semester_credits
        final_gpa.append(semester_gpa)

        print(f"Your GPA for Semester {semester}: {semester_gpa:.2f}\n")

    cgpa = sum(final_gpa) / semesters
    print(f"Your CGPA is: {cgpa:.2f}")


main();