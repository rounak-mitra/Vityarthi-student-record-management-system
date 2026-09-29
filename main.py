from student_manager import search_student, add_student, update_marks, display_all

def show_menu():
    print("\nStudent Record Management System")
    print("1. Search Student Record")
    print("2. Add New Student")
    print("3. Update Student Marks")
    print("4. View All Students")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            search_student()

        elif choice == "2":
            add_student()

        elif choice == "3":
            update_marks()

        elif choice == "4":
            display_all()

        elif choice == "5":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()