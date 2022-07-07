student_grades = input("Please input a list of student grades. ").split()

highest_grade = [0,0]
for indices, value in enumerate(student_grades):
    if int(value) > highest_grade[1]:
        highest_grade[1] = int(value)
        highest_grade[0] = indices

print(f'The highest grade is {highest_grade[1]} by student {highest_grade[0] + 1}')