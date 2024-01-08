# Simple Explanation of the Array
# Creating a simple Array and calculate the mean/Average of it

student_score = [90, 70, 93, 98, 77, 88, 89, 59, 67, 49, 45, 99, 100]
print("Default list:",student_score)

total_students = len(student_score)
print("Total Number of Students are: ",total_students)

# For loop to find the total marks
sum = 0
for total_marks in student_score:
    sum = sum + total_marks
print("Total Marks are: ",sum)

#Average
Average = sum/total_students
print("The average of the Marks is: ",Average)

#What if we need to update any value
#Like score 4 got 1 extra mark and we got one more students with 68 marks so for this
student_score[3] = student_score[3] + 1
student_score.append(68)
print("List after append and increment:",student_score)



