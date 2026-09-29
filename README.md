# Student Record Management System

A lightweight, modular Command Line Interface (CLI) application written in pure Python for managing university student profiles, course enrollments, and academic evaluations.

## Project Overview

The **Student Record Management System** is designed with a clear multi-module architecture that separates data storage, academic calculations, record management, user interaction, and unit testing into distinct Python modules.

### Key Features
- **Search Student Record:** Fast direct lookup by Student ID (case-insensitive) displaying complete profile info, individual marks, total score, percentage, and pass/fail status.
- **Register New Student:** Interactive form to add new student entries with validation for age, semester, residence type (Hosteller/Day Scholar), and individual subject scores.
- **Update Student Marks:** Modify existing subject marks with automatic recalculation of overall academic metrics.
- **View All Students:** Clean tabular summary displaying enrolled students along with their scores and results.
- **Automated Testing Suite:** Built-in unit test script (`test_system.py`) using `assert` statements to verify calculation accuracy.

---

## Modular File Structure

| File | Purpose |
| :--- | :--- |
| `main.py` | Interactive entry point and terminal menu loop. |
| `student_manager.py` | Core record operations (Search, Add, Update Marks, Display Summary). |
| `academic_engine.py` | Evaluation logic for totals, percentages, pass/fail status, and user input prompts. |
| `data_store.py` | Centralized in-memory dataset of student records. |
| `test_system.py` | Automated unit test suite verifying performance calculation logic. |
| `statement.md` | Formal problem statement, objectives, and project scope. |
| `README.md` | System documentation and execution instructions. |

---

## Academic Evaluation Logic

- **Subjects Evaluated:** Mathematics, Physics, and Computer Science (out of 100 each).
- **Passing Threshold:** A student passes if they score at least **40 marks in each individual subject** AND achieve an overall average percentage of **$\ge 40.0\%$**.
- **Calculation Rules:**
  $$\text{Total Marks} = \sum \text{Subject Scores}$$
  $$\text{Percentage} = \frac{\text{Total Marks}}{\text{Number of Subjects}}$$

---

## How to Run the Application

### Prerequisites
- Python 3.8 or higher installed on your system.

### 1. Launch the Main Application
Open your terminal in the project directory and execute:
```bash
python main.py