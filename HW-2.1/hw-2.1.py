# empty student list
students = []

# function to add students to the list
def add_student():
    full_name = input("Enter your full name: ")
    students.append(full_name)

# function to deleting students from the list
def delete_student():
    full_name = input("Enter the full name of the student that you want to delete: ")
    students.remove(full_name)

# function to add more than one student
def add_more_student():
    full_name = None
    print("If you do not want to add student enter 0")
    while full_name != "0":
        full_name = input("Enter student's full name: ")
        if full_name != "0":
            students.append(full_name)

# function to list all students
def list_students():
    for student in students:
        print(student)

# function to find student number
def student_number():
    student = input("Enter student name to find number: ")
    number = students.index(student)
    return number

# function to delete more than one student
def delete_more_student():
    full_name = None
    print("If you do not want to delete student enter 0")
    while full_name != "0":
        full_name = input("Enter student's full name: ")
        if full_name != "0":
            students.remove(full_name)

print("Adding a student")
add_student()

print("Adding more than one student")
add_more_student()

print("Student list")
list_students()

print("Deleting a student")
delete_student()

print("Student list")
list_students()

print("Finding a student number")
number = student_number()
print(number)

print("Delete more than one student")
delete_more_student()

print("Student list")
list_students()







