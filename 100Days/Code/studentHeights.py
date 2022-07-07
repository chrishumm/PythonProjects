student_heights = input("Enter students heights").split()
sum = 0
number_of_students = 0

for indices, value in enumerate(student_heights):
    sum += int(value)
    number_of_students +=1

average_height = sum / number_of_students
print(f"The average height is {int(average_height)}")
