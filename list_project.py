# Initialize an empty list to store student names
students = []

# Function to add a student to the list
def add_student(name):
    students.append(name)
    print(f'Student "{name}" added successfully!')

# Function to remove a student from the list
def remove_student(name):
    if name in students:
        students.remove(name)
        print(f'Student "{name}" removed successfully!')
    else:
        print(f'Student "{name}" not found!')

# Function to display all students
def display_students():
    if students:
        print("List of students:")
        for student in students:
            print(f'- {student}')
    else:
        print("No students to display.")

# Function to update a student's name
def update_student(old_name, new_name):
    if old_name in students:
        index = students.index(old_name)
        students[index] = new_name
        print(f'Student "{old_name}" updated to "{new_name}"!')
    else:
        print(f'Student "{old_name}" not found!')

# Function to sort the list of students
def sort_students():
    students.sort()
    print("Students sorted in ascending order.")

# Function to reverse the list of students
def reverse_students():
    students.reverse()
    print("Students list reversed.")

# Function to clear the list of students
def clear_students():
    students.clear()
    print("All students removed from the list.")

# Main function to display menu and take user input
def student_management_system():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a Student")
        print("2. Remove a Student")
        print("3. Update a Student")
        print("4. Display All Students")
        print("5. Sort Students")
        print("6. Reverse Students")
        print("7. Clear All Students")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter student name: ")
            add_student(name)

        elif choice == '2':
            name = input("Enter student name to remove: ")
            remove_student(name)

        elif choice == '3':
            old_name = input("Enter the current name of the student: ")
            new_name = input("Enter the new name: ")
            update_student(old_name, new_name)

        elif choice == '4':
            display_students()

        elif choice == '5':
            sort_students()

        elif choice == '6':
            reverse_students()

        elif choice == '7':
            clear_students()

        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the student management system
student_management_system()
