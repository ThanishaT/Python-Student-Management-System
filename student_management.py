# ==========================================
#       STUDENT MANAGEMENT SYSTEM
# ==========================================

students = []


# Add Student
def add_student():
    print("\n----- Add Student -----")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    phone = input("Enter Phone Number: ")

    marks = []
    print("\nEnter marks for 5 subjects:")

    for i in range(1, 6):
        mark = float(input(f"Enter Subject {i} Mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "department": department,
        "phone": phone,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


# Display Students
def display_students():
    print("\n----- Student Details -----")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\n----------------------------")
        print("Roll Number :", student["roll_no"])
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Department  :", student["department"])
        print("Phone       :", student["phone"])
        print("Marks       :", student["marks"])
        print("Total       :", student["total"])
        print("Average     :", student["average"])
        print("Grade       :", student["grade"])
        print("Result      :", student["result"])


# Search Student
def search_student():
    print("\n----- Search Student -----")

    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("----------------------------")
            print("Roll Number :", student["roll_no"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Department  :", student["department"])
            print("Phone       :", student["phone"])
            print("Marks       :", student["marks"])
            print("Total       :", student["total"])
            print("Average     :", student["average"])
            print("Grade       :", student["grade"])
            print("Result      :", student["result"])
            return

    print("Student not found.")


# Delete Student
def delete_student():
    print("\n----- Delete Student -----")

    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main Menu
while True:

    print("\n================================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.")