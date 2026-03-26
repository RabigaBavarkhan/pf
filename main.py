# a) Input & Variables
name = input("Enter student name: ")

math = float(input("Enter Math grade: "))
physics = float(input("Enter Physics grade: "))
python_grade = float(input("Enter Python grade: "))

# b) Calculations
average = (math + physics + python_grade) / 3
scholarship = 35000 if average >= 90 else 0
gpa = average / 25

# c) Formatted Output
print("\n==============================")
print("      STUDENT REPORT CARD")
print("==============================")
print(f"Student : {name}")
print(f"Math : {math}")
print(f"Physics : {physics}")
print(f"Python : {python_grade}")
print("------------------------------")
print(f"Average : {round(average, 2)}")
print(f"GPA : {round(gpa, 2)}")
print(f"Scholarship : {scholarship} KZT")
print("==============================")

# d) Comparison
print("Scholarship granted:", average >= 90)
print("Perfect score:", average == 100)