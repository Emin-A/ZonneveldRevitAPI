import random

# --- Rock, Paper, Scissors Game --------------------
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Making it as a list so that it can be chosen easily
game = [rock, paper, scissors]
decision = input(
    "Welcome to the Rock, Paper, Scissors Game!\nWhat do you choose?Type 0 for rock, 1 for paper, 2 for scissors.\n"
)
# create some way of randomly making a choice between rock, paper, scissors for the computer
human = int(decision[0])
# num_of_items = len(game)
# computer = random.randint(0, 3 - 1)
computer = random.choice(game)

# print(human)
# print(computer)
# compare that choice of computer against your choice
# then determining whether you won, lost, or its a draw.
if human == 0 and computer == game[0]:
    print(game[0])
    print(f"Computer chose:\n{game[0]}")
    print("It's a draw!")
elif human == 0 and computer == game[1]:
    print(game[0])
    print(f"Computer chose:\n{game[1]}")
    print("You lose!")
elif human == 0 and computer == game[2]:
    print(game[0])
    print(f"Computer chose:\n{game[2]}")
    print("You win!")
elif human == 1 and computer == game[0]:
    print(game[1])
    print(f"Computer chose:\n{game[0]}")
    print("You win!")
elif human == 1 and computer == game[1]:
    print(game[1])
    print(f"Computer chose:\n{game[1]}")
    print("It's a draw!")
elif human == 1 and computer == game[2]:
    print(game[1])
    print(f"Computer chose:\n{game[2]}")
    print("You lose!")
elif human == 2 and computer == game[0]:
    print(game[2])
    print(f"Computer chose:\n{game[0]}")
    print("You lose!")
elif human == 2 and computer == game[1]:
    print(game[2])
    print(f"Computer chose:\n{game[1]}")
    print("You win!")
elif human == 2 and computer == game[2]:
    print(game[2])
    print(f"Computer chose:\n{game[2]}")
    print("It's a draw!")
else:
    print("You typed an invalid number! Game Over!")
