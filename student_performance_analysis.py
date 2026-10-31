
import numpy as np

print("=" * 50)
print("     STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 50)

# Enter the number of students
n = int(input("\nEnter the number of students: "))

if n <= 0:
    print("Please enter at least one student.")
    raise SystemExit

subjects = ["Python", "DBMS", "Mathematics", "English", "Computer Networks"]

names = []
marks_list = []

# Input student details
for i in range(n):
    print(f"\nEnter details for Student {i + 1}")
    name = input("Enter student name: ").strip()

    if not name:
        name = f"Student {i + 1}"

    names.append(name)

    student_marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks in {subject} (0-100): "))

                if 0 <= mark <= 100:
                    student_marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    marks_list.append(student_marks)

# Convert marks into a NumPy array
marks = np.array(marks_list)

# Calculate total, percentage and average
totals = np.sum(marks, axis=1)
percentages = np.mean(marks, axis=1)
averages = np.mean(marks, axis=1)

# Calculate subject-wise class averages
subject_averages = np.mean(marks, axis=0)

# Calculate grades
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

grades = [calculate_grade(p) for p in percentages]

# Identify pass/fail
# A student must score at least 35 in every subject to pass
results = np.all(marks >= 35, axis=1)

# Find the topper
topper_index = np.argmax(percentages)

# Display individual student results
print("\n" + "=" * 85)
print("                     STUDENT RESULT REPORT")
print("=" * 85)

print(f"{'Name':<20}{'Total':>10}{'Percentage':>15}"
      f"{'Grade':>12}{'Result':>12}")
print("-" * 85)

for i in range(n):
    result = "PASS" if results[i] else "FAIL"

    print(f"{names[i]:<20}{totals[i]:>10.1f}"
          f"{percentages[i]:>14.2f}%"
          f"{grades[i]:>12}{result:>12}")

# Display class analysis
print("\n" + "=" * 50)
print("              CLASS ANALYSIS")
print("=" * 50)

print(f"Total students       : {n}")
print(f"Class average        : {np.mean(percentages):.2f}%")
print(f"Highest percentage   : {np.max(percentages):.2f}%")
print(f"Lowest percentage    : {np.min(percentages):.2f}%")
print(f"Standard deviation   : {np.std(percentages):.2f}")
print(f"Students passed      : {np.sum(results)}")
print(f"Students failed      : {np.sum(~results)}")
print(f"Class pass percentage: {np.mean(results) * 100:.2f}%")

print(f"\nClass Topper: {names[topper_index]}")
print(f"Topper Percentage: {percentages[topper_index]:.2f}%")

# Display subject-wise averages
print("\n" + "=" * 50)
print("           SUBJECT-WISE AVERAGES")
print("=" * 50)

for i, subject in enumerate(subjects):
    print(f"{subject:<22}: {subject_averages[i]:.2f}")

# Identify students who need improvement
print("\n" + "=" * 50)
print("          STUDENTS NEEDING SUPPORT")
print("=" * 50)

found = False

for i in range(n):
    if not results[i]:
        weak_subjects = [
            subjects[j]
            for j in range(len(subjects))
            if marks[i, j] < 35
        ]

        print(f"{names[i]} needs improvement in: "
              f"{', '.join(weak_subjects)}")
        found = True

if not found:
    print("All students passed every subject!")

print("\nAnalysis completed successfully.")
print("=" * 50)
