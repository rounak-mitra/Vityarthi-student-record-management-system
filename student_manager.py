from data_store import students
from academic_engine import calculate_academic_performance, prompt_marks_input

def search_student():
    sid = input("\nEnter Student ID to search (e.g. VIT001): ").strip().upper()
    if sid in students:
        s = students[sid]
        tot, pct, res = calculate_academic_performance(s["marks"])
        
        print("\n" + "="*40)
        print(f" STUDENT DETAILS - {sid}")
        print("="*40)
        print(f" Name       : {s['name']}")
        print(f" Age        : {s['age']}")
        print(f" State      : {s['state']}")
        print(f" Course     : {s['course']} (Sem {s['semester']})")
        print(f" Residence  : {'Hosteller' if s['is_hosteller'] else 'Day Scholar'}")
        print("-" * 40)
        print(" Marks:")
        for sub, score in s['marks'].items():
            print(f"   {sub:<10}: {score}")
        print("-" * 40)
        print(f" Total      : {tot} / 300")
        print(f" Percentage : {pct}%")
        print(f" Result     : {res}")
        print("="*40)
    else:
        print(f"\n[!] Student ID '{sid}' not found.")

def add_student():
    print("\n--- Register New Student ---")
    sid = input("Enter New Student ID (e.g. VIT006): ").strip().upper()
    if sid in students:
        print("[!] Error: Student ID already exists.")
        return

    name = input("Enter Full Name: ").strip()
    
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        age = 18

    state = input("Enter Home State: ").strip()
    course = input("Enter Course: ").strip()
    
    try:
        sem = int(input("Enter Semester: "))
    except ValueError:
        sem = 1
        
    res_choice = input("Is Hosteller? (y/n): ").strip().lower()
    hosteller = True if res_choice == 'y' else False

    marks = prompt_marks_input()

    # save new student record
    students[sid] = {
        "name": name,
        "age": age,
        "state": state,
        "course": course,
        "semester": sem,
        "is_hosteller": hosteller,
        "marks": marks
    }
    print(f"\n[+] Student '{name}' ({sid}) registered successfully!")

def update_marks():
    sid = input("\nEnter Student ID to update marks: ").strip().upper()
    if sid in students:
        print(f"Updating marks for {students[sid]['name']} ({sid}):")
        new_m = prompt_marks_input()
        students[sid]["marks"] = new_m
        print("\n[+] Marks updated successfully!")
    else:
        print(f"\n[!] Student ID '{sid}' not found.")

def display_all():
    print("\n" + "="*85)
    print(f"{'ID':<8} {'Name':<18} {'Course':<8} {'Sem':<5} {'Total':<7} {'Pct':<8} {'Result':<6}")
    print("="*85)
    
    for sid, info in students.items():
        tot, pct, res = calculate_academic_performance(info["marks"])
        print(f"{sid:<8} {info['name']:<18} {info['course']:<8} {info['semester']:<5} {tot:<7} {pct:<8}% {res:<6}")
        
    print("="*85)