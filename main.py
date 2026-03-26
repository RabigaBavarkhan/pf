# A Input
name = input("Enter student name: ")

math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python_grade = float(input("Enter Python grade: "))

# B Calculations
average = (math + physics + python_grade) / 3
gpa = average / 25
scholarship = 35000 if average >= 90 else 0

# Output 
print("==============================")
print("      STUDENT REPORT CARD")
print("==============================")
print("Student : " + name)
print("Math : " + str(math))
print("Physics : " + str(physics))
print("Python : " + str(python_grade))
print("------------------------------")
print("Average : " + str(round(average, 2)))
print("GPA : " + str(round(gpa, 2)))
print("Scholarship : " + str(scholarship) + " KZT")
print("==============================")

# Comparison
print("Scholarship granted:", average >= 90)
print("Perfect score:", average == 100)