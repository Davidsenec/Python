import random

# A function that asks the player for their choice
def getchoice():
    p_choice = input("Choose your weapon!:").strip().lower()
    options = ["rock", "paper", "scissors"]

    # validates the input
    while p_choice not in options:
        print("Invalid input. Try again.")
        p_choice = input("Choose your weapon!:").strip().lower()

    c_choice = random.choice(options)
    choices =  {"Player":p_choice, "Computer":c_choice}

    return choices  

# A function that checks if the player wins or loses
def checkwin(Player, Computer):
    print(f"You chose {Player}, the computer chose {Computer}")
    if Player == Computer:
        return "Draw"
    elif Player == "rock":
        if Computer == "scissors":
            return "Rock destroys scissors. You Win!"
        elif Computer == "paper":
            return "Paper beats Rock. You lose STUPID!"
    elif Player == "scissors":
        if Computer == "paper":
            return "scissors cuts paper. You Win!"
        elif Computer == "rock":
            return "Rock destroys scissors. You lose STUPID!"
    elif Player == "paper":
        if Computer == "rock":
            return "Paper beats Rock. You Win!"
        elif Computer == "scissors":
            return "scissors cuts paper. You lose STUPID!"


# Prints the welcome message
print("Welcome to Rock Paper Scissors!")

# Asks the player for their choice
choices = getchoice()
# calls the win condition function
result = checkwin(choices["Player"], choices["Computer"])

# Prints what the player chose along with the computer and who wins
print(choices)
print(result)