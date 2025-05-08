import random

# Mapping choices
youDict = {"r": 0, "p": 1, "s": 2}
mainDict = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Taking user input
yourChoice = input("Enter your choice (r for Rock / p for Paper / s for Scissors): ").lower()

if yourChoice not in youDict:
    print("Invalid input! Please choose r, p, or s.")
else:
    you = youDict[yourChoice]
    computer = random.choice([0, 1, 2])

    print(f"\nYou chose {mainDict[you]}")
    print(f"Computer chose {mainDict[computer]}")

    # Result logic
    if you == computer:
        print("It's a draw!")
    elif (you == 0 and computer == 2) or (you == 1 and computer == 0) or (you == 2 and computer == 1):
        print("Hurray!! You Win! :)")
    else:
        print("Oh!! You Lose! :(")
