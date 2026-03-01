# Advanced Rock Paper Scissors Game

import random

def get_computer_choice(user_choice, level):
    choices = ["rock", "paper", "scissors"]
    
    if level == "1":  # Easy mode (random)
        return random.choice(choices)
    
    elif level == "2":  # Hard mode (simple AI logic)
        # Computer tries to beat the user choice
        if user_choice == "rock":
            return "paper"
        elif user_choice == "paper":
            return "scissors"
        else:
            return "rock"

def decide_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "User"
    else:
        return "Computer"

def play_game():
    user_score = 0
    computer_score = 0
    total_rounds = 0
    ties = 0

    print("Rock Paper Scissors Game")
    print("Select Difficulty Level")
    print("1. Easy")
    print("2. Hard")

    level = input("Enter your choice (1/2): ")

    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user_choice == "exit":
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again.")
            continue

        computer_choice = get_computer_choice(user_choice, level)
        result = decide_winner(user_choice, computer_choice)

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        total_rounds += 1

        if result == "Tie":
            print("Round Result: Tie")
            ties += 1
        elif result == "User":
            print("Round Result: You Win")
            user_score += 1
        else:
            print("Round Result: Computer Wins")
            computer_score += 1

        print("Current Score -> You:", user_score, "| Computer:", computer_score)

    print("\nGame Summary")
    print("Total Rounds Played:", total_rounds)
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    print("Ties:", ties)

    if user_score > computer_score:
        print("Final Result: You won the game.")
    elif computer_score > user_score:
        print("Final Result: Computer won the game.")
    else:
        print("Final Result: Game ended in a tie.")

if __name__ == "__main__":
    play_game()