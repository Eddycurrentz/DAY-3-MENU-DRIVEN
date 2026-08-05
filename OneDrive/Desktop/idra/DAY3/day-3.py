# Basic Student Management System

students = []  # list to store student records

def add_student():
    ID = input("Enter ID: ")
    Name = input("Enter Name: ")
    Age = input("Enter Age: ")
    Course = input("Enter Course: ")
    Marks = input("Enter Marks: ")
    student = {"ID": ID, "Name": Name, "Age": Age, "Course": Course, "Marks": Marks}
    students.append(student)
    print("Student added!\n")

def view_students():
    for s in students:
        print(s)

def search_student():
    key = input("Enter ID or Name to search: ")
    for s in students:
        if s["ID"] == key or s["Name"].lower() == key.lower():
            print("Found:", s)
            return
    print("Not found!\n")

def update_student():
    ID = input("Enter ID to update: ")
    for s in students:
        if s["ID"] == ID:
            s["Name"] = input("Enter new Name: ")
            s["Age"] = input("Enter new Age: ")
            s["Course"] = input("Enter new Course: ")
            s["Marks"] = input("Enter new Marks: ")
            print("Student updated!\n")
            return
    print("ID not found!\n")

def delete_student():
    ID = input("Enter ID to delete: ")
    for s in students:
        if s["ID"] == ID:
            students.remove(s)
            print("Student deleted!\n")
            return
    print("ID not found!\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice!\n")

menu()
