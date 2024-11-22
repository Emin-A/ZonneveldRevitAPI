# ---LOOPS----------------------------------------------------------------
# ---FOR LOOP---

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# ---Challenge 01 --------------
# Write a program that calculates the average student height from a List of heights.
# The average height can be calculated by adding all the heights together and dividing
# by the total number of heights.
# You also need to round the number using the round() function.
# You can't use len() or sum()!!!
# Try to replicate their functionality using what you have leant about loops.

# This is just to input the list of heights:
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Use a for loop to add each of the item inside of the list together,
# Use a for loop to determine how many items there are in the list and then
# Use a for loop to figure out the average
# Then round it to nearest whole number

# print(type(student_heights))   the type is a list
# print(type(student_heights[n]))   the type is a integer
# print(student_heights[n])   prints how many items there are

total_height = 0  # This was needed to get the sum function
for height in student_heights:
    total_height += height
    # average = total_height / n
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(
    total_height / number_of_students
)  # This was needed for the average function
print(average_height)

# for n in student_heights:
#     n = sum(student_heights) / student_heights[n - 1]
# print(n)
