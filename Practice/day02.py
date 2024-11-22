# Data Types

# String

# print("Hello"[-1])  # it is "o"

# print("123" + "345")  # it didn't calculate

# Integer

# print(123 + 345)  # actually calculated

# # Float

# 3.14159  # when there is decimal point

# # Boolean

# True
# False

# # Type, Type error, Type conversion

# num_char = len(input("What is your name?"))

# new_num_char = str(num_char)  # we convert it to a string

# print(
#     "Your name had " + new_num_char + " characters."
# )  # cant concatenate string with integer

# # Check the type
# a = str(123)
# print(type(a))

# b = float(123)
# print(type(b))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# # Write a program that adds the digits in a 2 digit number.
# two_digit_number = input("Type a two digit number: ")
# num_one = int(two_digit_number[0])
# num_two = int(two_digit_number[1])
# num_total = num_one + num_two
# print(num_total)

# # Math operations (!!! PEMDASLR priority order: (), **, * , /, + , -)
# 3 + 5
# 7 - 4
# 3 * 2
# print(type(6 / 3))
# 2**3  # 2 to the power of 3

# print(3 * 3 + 3 / 3 - 3)  # 7
# print(3 * (3 + 3) / 3 - 3)  # 3.0
# print(3 / 3 + 3 * 3 - 3)  # 7.0, division started first not multiplication

# BMI Calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# first = float(height)
# second = int(weight)

# bmi = second / first**2
# print(round(int(bmi)))

print(int(8 / 3))  # 2
print(round(8 / 3))  # 3
print(round(8 / 3, 2))  # round it to 2 decimal places 2.67
print(round(2.66666, 2))  # 2.67

print(8 // 3)  # 2 flow division - whole number without decimals
print(type(8 // 3))  # int
print(type(8 / 3))  # float
print(type(4 / 2))  # float

# ---- ( += , -=, *=, /=, //)

result = 4 / 2
result /= 2
print(result)  # 1.0

score = 0
score += 1
print(score)  # 1

# f - string
# rezultat = 0
# visina = 1.89
# isWinning = True
# print(
#     f"your score is {rezultat}, your height is {visina}, you are winning is {isWinning}."
# )

# ------Challenge 2
# 1 year = 365 days, 1 year = 52 week, 1 year = 12 months
# How many days, weeks, months you have left until 90 years old.
# Round the result to the nearest whole number.
# age = input("What is your current age: \n")
# age_left = 90 - int(age)
# z = 12 * age_left
# y = 52 * age_left
# x = 365 * age_left

# print(f"You have {x} days, {y} weeks, {z} months left.")

# ------Challenge 3 Tip Calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12
# 12 / 100 = 0.12
# 150 * 0.12 = 18.0
# 150 + 18 = 168
# shortcut 150 * 1.12 = 168.000000000000003
# 168 / 5 = 33.6  (divide it to 5 people)
# Now round it to 2 decimal places, 33.60
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
calcOne = bill * (tip / 100 + 1)
people = int(input("How many people to split the bill?\n"))
calcTwo = calcOne / people
# print(f"Each person should pay: ${round(calcTwo,2)}")
# or
final_amount = "{:.2f}".format(calcTwo)
print(f"Each person should pay: ${final_amount}")


# print(f"Each person should pay:\n{}")
