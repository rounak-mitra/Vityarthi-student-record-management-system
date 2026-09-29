# Problem Statement: Student Record Management System

## Project Context & Background
Educational institutions and university departments require reliable tools to manage student personal details and calculate academic evaluations accurately. Performing calculations manually or managing student details across unorganized spreadsheets frequently introduces errors in subject totals, percentage calculations, and pass/fail determinations.

## Problem Definition
Manual and unstructured student record tracking faces several key challenges:
1. **Human Error in Calculations:** Computing subject totals, percentage averages, and minimum-passing thresholds manually is error-prone.
2. **Inconsistent Data Structuring:** Unstandardized storage formats cause data discrepancies and slow down record retrieval.
3. **Inefficient Search Capabilities:** Searching for specific student details in unindexed sheets or physical logs is slow and cumbersome.

## Project Objectives
The objective of this project is to develop a lightweight, modular Command Line Interface (CLI) application in pure Python that:
- Maintains an in-memory database of student profiles and academic scores.
- Implements direct record lookup by Student ID (e.g., `VIT001`).
- Provides interactive capabilities to register new students and update existing subject marks.
- Dynamically computes total marks, overall percentage, and pass/fail status based on institutional passing criteria (minimum 40 marks per subject and an overall percentage of $\ge 40.0\%$).
- Formats multi-student summaries into readable tabular outputs.
- Integrates automated unit tests using Python `assert` statements to verify calculation accuracy.

## Scope of Implementation
- **Data Layer:** Centralized in-memory dataset (`data_store.py`) containing student demographic profiles and academic scores across three core subjects: Mathematics, Physics, and Computer Science.
- **Business Logic Layer:** Dedicated academic calculation engine (`academic_engine.py`) and record management module (`student_manager.py`).
- **User Interface Layer:** Interactive, menu-driven terminal interface (`main.py`).
- **Verification Layer:** Automated unit test suite (`test_system.py`) testing pass and fail evaluation conditions.