student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
def student_status(value):
    if value >= 91 and value <= 100:
        return 'Outstanding'
    if value >= 81 and value <= 90:
        return 'Exceeds Expectations'
    if value >= 71 and value <= 80:
        return 'Acceptable'
    return 'Fail'

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student_grades[key] = student_status(student_scores[key])
    

# 🚨 Don't change the code below 👇
print(student_grades)