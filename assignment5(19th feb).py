
student_map = {}

for i in range(5):
    name = input("enter name: ")
    marks = int(input("enter marks: "))
    student_map[name] = marks


# FOR TOPPERS
# WHAT IF THERE ARE TWO OR MORE TOPPERS
# AFTER FINDING THE MAX MARKS TRY GETTING THE NAME OF THE TOPPER

max_marks = 0
toppers = []
total = 0
grades = {}

for name, marks in student_map.items():
    
    total += marks

    if marks > max_marks:
        max_marks = marks
        toppers = [name]
    elif marks == max_marks:
        toppers.append(name)

    # ASSIGN GRADES
    if marks >= 90:
        grades[name] = "A"
    elif marks >= 75:
        grades[name] = "B"
    elif marks >= 60:
        grades[name] = "C"
    else:
        grades[name] = "D"

average = total / 5


print("Topper Marks:", max_marks)
print("Topper(s):", toppers)
print("average marks is:", average)
print("Grades:", grades)  