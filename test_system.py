from academic_engine import calculate_academic_performance

def run_tests():
    print("Testing academic performance...")

    # Test 1: Student passes
    marks = {"Math": 80, "Physics": 75, "CS": 85}
    total, percentage, result = calculate_academic_performance(marks)

    assert total == 240
    assert percentage == 80.0
    assert result == "Pass"

    print("Pass test successful")

    # Test 2: Student fails
    marks = {"Math": 35, "Physics": 75, "CS": 85}
    total, percentage, result = calculate_academic_performance(marks)

    assert result == "Fail"

    print("Fail test successful")
    print("All tests completed!")

if __name__ == "__main__":
    run_tests()
