
import numpy as np

# 1. Create grade matrix
np.random.seed(2026)
grades = np.random.randint(0, 101, size=(200, 8))

# 2. Statistics
student_avg = grades.mean(axis=1)
course_avg = grades.mean(axis=0)

overall_stats = {
    "mean": grades.mean(),
    "std": grades.std(),
    "min": grades.min(),
    "max": grades.max()
}

# 3. Apply curve
curve_mask = course_avg < 50
curved_grades = grades + (curve_mask * 10)
curved_grades = np.clip(curved_grades, 0, 100)

# 4. Letter grades
letter_grades = np.where(
    curved_grades >= 90, "A",
    np.where(
        curved_grades >= 80, "B",
        np.where(
            curved_grades >= 70, "C",
            np.where(curved_grades >= 60, "D", "F")
        )
    )
)

# 5. Top 10 students
curved_student_avg = curved_grades.mean(axis=1)
top10_indices = np.argsort(curved_student_avg)[-10:][::-1]

# 6. Students passing all courses
passing_students_mask = np.all(curved_grades >= 60, axis=1)
num_passing_students = passing_students_mask.sum()

print("Per-course averages (before curve):")
print(np.round(course_avg, 2))

print("\nCourses getting curve:")
print(np.where(curve_mask)[0])

print("\nTop 10 student indices:")
print(top10_indices)

print("\nStudents passing all courses:")
print(f"{num_passing_students} out of 200")
