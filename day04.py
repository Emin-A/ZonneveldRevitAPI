import random

# import my_module

# random_integer = random.randint(0, 5)
# print(random_integer)
# print(my_module.pi)

# 0.0000000000 - 0.9999999999
# random_float = random.random()
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# ---- Coding Challenge 1 --------------------------------
# HEADS or TAILS coin toss
# first letter should be capitalized and spelt exactly (Heads not heads)
# Generate a random number either 0 or 1.
# Use that number to print out Heads or Tails. (1 means Heads, 0 means Tails)

# rand_num = random.randint(0, 1)
# if rand_num == 0:
#     print("0 means Tails!")
# if rand_num == 1:
#     print("1 means Heads!")

# --- LISTS ----------------------------------------------------------------
# states_of_america = [
#     "Delaware",
#     "Pennsylvania",
#     "South Carolina",
#     "Michigan",
#     "Nebraska",
# ]
# print(states_of_america[-1])

# changing item
# states_of_america[1] = "Michigan"
# print(states_of_america)

# add item at the end of a list
# states_of_america.append("Angelaland")
# print(states_of_america)

# extend the list
# states_of_america.extend(["Idiotikus", "Popokopoluss"])
# print(states_of_america)

# ---Coding Challenge 02 ------------------------
# Select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# You are NOT allowed to use the 'choice()' function!
# You will have to use the '.split(",")' function
# You might need the help of the 'len()' function.

# names_string = input("Give me everybody's names, separated by a comma.\n")
# names = names_string.split(", ")
# print(names)

# We need to have the total number of names
# num_items = len(names)
# this isn't correct, because we dont know how many names there will be
# choice = names[(random.randint(0, 5))]
# Now its Correct!
# choice = names[random.randint(0, num_items - 1)]

# now i need to know how to print the item name as string not integer
# print(f"{choice} is going to buy the meal today!")

# --- NESTED LIST --------------------------------
# dirty_dozen example
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = [
#     "Strawberries",
#     "Nectarines",
#     "Apples",
#     "Grapes",
#     "Peaches",
#     "Cherries",
#     "Pears",
# ]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# --- Coding Challenge 03 ----------------------------------------------------------------
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
