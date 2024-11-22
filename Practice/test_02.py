print(
    """  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/"""
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are on an island in search of a treasure!\nThere two paths in front of you.")
print(
    "The left one goes through a dense jungle and the right one goes through a path full of crevaces!"
)
print("If you stay, a hideous monster will kill you!")
choice_one = input("Whats it gonna be? Left, Right or Stay?\n")

if choice_one == "Left".lower():
    print("You are going through a dense jungle path, there is a river...")
    choice_two = input("Will you swim, wait or do nothing?\n")
    if choice_two == "Swim".lower():
        print(
            "You swam half way but a giant river monster swallowed you up!\nGAME OVER."
        )
    elif choice_two == "Wait".lower():
        print(
            "You waited for a moment and looked around... there is a blue, red and a yellow door."
        )
        choice_three = input(
            "Do you want to wait or choose one of the doors?\nWhat's it gonna be: blue, red or yellow door?\n"
        )
        if choice_three == "Blue".lower():
            print(
                "You opened the blue door but a bunch of monsters ate you alive!\nGAME OVER."
            )
        elif choice_three == "Red".lower():
            print(
                "You opened the red door but a blast of scorching fire burnt you alive instantly!\nGAME OVER."
            )
        elif choice_three == "Yellow".lower():
            print(
                "You opened the yellow door, your found the treasure chest!\nYOU WIN!"
            )
        else:
            print(
                "You waited and you didn't do anything so the hideous monsters sliced your spinal cord!\nGAME OVER."
            )
    else:
        print(
            "You didn't do anything so the hideous monsters tor your body apart!\nGAME OVER."
        )
elif choice_one == "Right".lower():
    print("You fell into a crevace full of spikes and died brutally!!! \nGAME OVER.")
else:
    print(
        "You stayed and fought bravely with the hideous monster... but eventually it cut of your head! \nGAME OVER."
    )
