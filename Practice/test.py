# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

# print("Hello world!\nHello world!\nHello world!")
# print("Hello" + " Emin")

# print(
#     'Day 1 - String Manipulation\nString Concatenation is done with the "+" sign.\ne.g. print("Hello " + "world")\nNew lines can be created with a backslash and n.'
# )

# input("What is your name?")
# print("Hello " + input("What is your name?"))

# Add your name in the input field so that the output shows the total number of characters.
# Emin = 4 character
# print(len(input("What is your name? ")))

# name = "Jack"
# print(name)

# name = "Jimmy"
# print(name)

# name = input("What is your name?")
# length = len(name)
# print(length)

# ---Exercise 1----
# Make two variables "a" and "b".
# when printing the variable "a" must show the value of "b" and vice versa.
# you might need to make some more variables.

# a = input("a:")
# b = input("b:")

# c = a
# a = b
# b = c

# print("a = " + a)
# print("b = " + b)

# ---------------------------------------
# -------- PROJECT 1 --------------------
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line.
print(
    "Greetings and welcome to project BandNameGenerator! Please answer the following questions!"
)
nameCity = input("What is the name of the city you were born in?\n")
namePet = input("What is the name of your pet?\n")
print("This is the name of your band:\n" + nameCity + namePet)
