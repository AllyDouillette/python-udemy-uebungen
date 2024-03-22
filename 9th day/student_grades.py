student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
def pointsToGrade(points):
    if (points >= 91):
        return "Outstanding"
    elif (points >= 81):
        return "Exceeds Expectations"
    elif (points >= 71):
        return "Acceptable"
    else:
        return "Fail"

for student in student_scores:
    points = student_scores[student]
    student_grades[student] = pointsToGrade(points)

# 🚨 Don't change the code below 👇
print(student_grades)