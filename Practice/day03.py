# Control flow with "if else" and Conditional Statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ---Modulo operator "%" (it gives you the remainder after a division)
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2, with no remainder!
# if division is clean then it is an even, if not then it is a remainder.

# number = int(input("Which number do you want to check?"))

# if the number is divisible by 2 with 0 remainder
# if number % 2 == 0:
#     print("It is an even number!")
# else:
#     print("It is an odd number!")

# --- Nested if statements and elif statements ---
# if condition:
#    if another condition:
#        do this
#    else:
#        do this
# else:
#    do this

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ---Code challenge 2 BMI 2.0 ---

# height = float(input("enter your height in m:\n"))
# weight = float(input("enter your weight in kg:\n"))

# bmi = round(weight / height**2)
# print("Your BMI is " + round(int(bmi)))

# if bmi <= 18.5:
#     print(
#         f"Your BMI is {bmi} which is below 18.5, this means you are "
#         + "\033[1munderweight!\033[0m"
#     )
# elif bmi >= 18.5 and bmi <= 25:
#     print(
#         f"Your BMI is {bmi} which is in the range of 18.5 and 25, this mean you have a "
#         + "\033[1mnormal weight!\033[0m"
#     )
# elif bmi >= 25 and bmi <= 30:
#     print(
#         f"Your BMI is {bmi} which is in the range of 25 and 30, this means you are "
#         + "\033[1moverweight!\033[0m"
#     )
# elif bmi >= 30 and bmi <= 35:
#     print(
#         f"Your BMI is {bmi} which is in the range of 30 and 35, this means you are "
#         + "\033[1mobese!\033[0m"
#     )
# else:
#     print(
#         "Your BMI is above 35, which means you are " + "\033[1mclinically obese!\033[0m"
#     )

# ---- Code Challenge 3 Leap Year --------
# Write a program that asks for a year and gives you if it is a leap year or not.
# A normal year has 365 days.
# A leap year has 366 days with an extra Friday in February.
# The year 2000:
# 2000 / 4 = 500 (Leap)
# 2000 / 100 = 20 (Not leap)
# 2000 / 400 = 5 (Leap!)
# So the year 2000 is a leap year.

# year = int(input("Which year do you want to check?\n"))

# if year % 4 == 0:
#     print(f"The year {year} is a leap year!")
# elif year % 100 == 1:
#     print(f"The year {year} is NOT a leap year!")
# elif year % 400 == 2:
#     print(f"Ok!Now the year {year} is a leap year!")
# else:
#     print(f"So the year {year} is definitely NOT a leap year!")

# Or you go if, if, if, then else,else,else

# ---Going back to the Rollercoaster but now with "Multiple if else" ----

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         # Add $3 to their bill
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# --- Code Challenge 04 ----------------------------------------------------------------
# Congratulations, you've got a job at Python Pizza. Your first job is to build an
# automatic pizza order program.
# "Small pizza: $15"
# "Medium pizza: $20"
# "Large pizza: $25"
#
# Pepperoni for small pizza: +$2
# Pepperoni for medium or large pizza: +$3
#
# Extra cheese for any size pizza: +$1

# print("Welcome to Python Pizza!!!")
# size = input("Which size of pizza do you want to order?(S-Small, M-Medium, L-Large):\n")
# bill = 0

# if size == "S":
#     bill = 15
# if size == "M":
#     bill = 20
# if size == "L":
#     bill = 25
# pepperoni = input("Would you like extra pepperoni?(Y/N)\n")
# if pepperoni == "Y" and size == "S":
#     bill += 2
# if pepperoni == "Y" and size == "M" or pepperoni == "Y" and size == "L":
#     bill += 3
# cheese = input("Would you like extra cheese?(Y/N)\n")
# if cheese == "Y":
#     bill += 1
# print(f"Your final bill is: ${bill}.")

# Is there another way I can write the code above with (Nested if else)!!!

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S,M,L\n")
# add_pepperoni = input("Do you want pepperoni? Y/N\n")
# extra_cheese = input("Do you want extra cheese? Y/N\n")

# bill = 0
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#         if extra_cheese == "Y":
#             bill += 1
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
# elif size == "L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
# print(f"Your final bill is: ${bill}.")

# --- Write it again in another way ---

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S,M,L\n")
# add_pepperoni = input("Do you want pepperoni? Y/N\n")
# extra_cheese = input("Do you want extra cheese? Y/N\n")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# ----- Adding logical operators "and", "or" ,"not" to rollercoaster exercise ------------

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Free ride!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         # Add $3 to their bill
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ---- Coding Exercise - Love Calculator --------------------------------
# Take both peoples names and check the number of times the letters in the word TRUE occurs.
# Then check for the number of time the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# For love scores "less than 10" or "greater than 90", the message should be:
# "YOur score is "x", you go together like coke and mentos!"

# For Love scores "between 40" and "50", the message should be:
# "Your score is "x", you are alright together."

# Otherwise, the message will just be their score e.g.:
# "Your score is "z"."

# name1 = "Angela Yu"
# name2 = "Jack Bauer"

# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53
# Print: "Your score is 53."

# tip1. Use the "lower()" function to change all the letters in a string to lower case
# tip2. Use the "count()" function will give you the number of times a letter occurs in a string.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_cased = combined_string.lower()

letter_one = lower_cased.count("t")
letter_two = lower_cased.count("r")
letter_three = lower_cased.count("u")
letter_four = lower_cased.count("e")
letter_five = lower_cased.count("l")
letter_six = lower_cased.count("o")
letter_seven = lower_cased.count("v")
letter_eight = lower_cased.count("e")

print(
    f"T occurs {letter_one} times.\nR occurs {letter_two} times.\nU occurs {letter_three} times.\nE occurs {letter_four} times."
)
print(f"Total = {letter_one+letter_two+letter_three+letter_four}\n")
print(
    f"L occurs {letter_five} times.\nO occurs {letter_six} times.\nV occurs {letter_seven} times.\nE occurs {letter_eight} times."
)
print(f"Total = {letter_five+letter_six+letter_seven+letter_eight}\n")
# Total number summed
sum_one = letter_one + letter_two + letter_three + letter_four
sum_two = letter_five + letter_six + letter_seven + letter_eight
sum_score = int(str(sum_one) + str(sum_two))

if (sum_score < 10) or (sum_score > 90):
    print(f"Your score is {sum_score}%, you go together like coke and mentos!")
elif (sum_score >= 40) and (sum_score <= 50):
    print(f"Your score is {sum_score}%, you are alright together!")
else:
    print(f"Your score is {sum_score}%.")
