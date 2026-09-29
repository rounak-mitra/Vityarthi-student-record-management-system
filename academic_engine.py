# Academic evaluation engine

def calculate_academic_performance(marks_dict):
    # return zeros if no marks passed
    if not marks_dict:
        return 0, 0.0, "N/A"
    
    # calculate total
    total_marks = 0
    for sub in marks_dict:
        total_marks += marks_dict[sub]
    
    # calculate average
    num_subjects = len(marks_dict)
    percentage = round(total_marks / num_subjects, 2)
    
    # check if student passed every subject (min 40)
    is_pass = True
    for sub in marks_dict:
        if marks_dict[sub] < 40:
            is_pass = False
            break
            
    # overall result decision
    if is_pass and percentage >= 40.0:
        status = "Pass"
    else:
        status = "Fail"
        
    return total_marks, percentage, status


def prompt_marks_input():
    subjects = ["Math", "Physics", "CS"]
    marks = {}
    print("\nEnter subject marks (out of 100):")
    
    for sub in subjects:
        while True:
            try:
                score = int(input(f"  {sub}: "))
                if score >= 0 and score <= 100:
                    marks[sub] = score
                    break
                else:
                    print("  [!] Marks should be between 0 and 100.")
            except ValueError:
                print("  [!] Please enter numbers only.")
                
    return marks