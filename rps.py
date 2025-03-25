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
    player_choices = {"Player": p_choice, "Computer": c_choice}

    return player_choices


# A function that checks if the player wins or loses
def check_win(player, computer):
    print(f"You chose {player}, the computer chose {computer}")
    if player == computer:
        return "Draw"
    elif player == "rock" and computer == "scissors" or \
            player == "scissors" and computer == "paper" or \
            player == "paper" and computer == "rock":
        return f"{player} beats {computer} You Win!"
    else:
        return f"{computer} beats {player} You Lose STUPID!"


# Prints the welcome message
print("Welcome to Rock Paper Scissors!")

# Asks the player for their choice
choices = getchoice()
# calls the win condition function
result = check_win(choices["Player"], choices["Computer"])

# Prints what the player chose along with the computer and who wins
print(choices)
print(result)
