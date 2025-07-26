# Rock, Paper, Scissors 🗿📄✂️
# Implement the classic game where the user plays against the computer.
# •	Description: The user chooses rock, paper, or scissors. The computer makes a random choice.
# The program then determines and announces the winner based on the game's rules
# (Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock).
# •	Concepts Covered: random module (specifically random.choice()), lists, if/elif/else statements,
# and handling user input.
# •	Next Step: Keep score over multiple rounds and declare an overall winner after
# a certain number of games (e.g., best of five).
import random
def rps():
    choice=random.choice("rpc")
    user_choice=input("Enter Your Choice Rock(r), Paper(p), Scissor(c): ")
    if user_choice==choice:
        print("Tie")
    elif user_choice=="r" and choice=="p":
        print("You Won")
    elif user_choice=="r" and choice=="c":
        print("You Lost")
    elif user_choice=="p" and choice=="r":
        print("You Lost")
    elif user_choice=="p" and choice=="c":
        print("You Lost")
    elif user_choice=="c" and choice=="p":
        print("You Won")
    elif user_choice=="c" and choice=="r":
        print("You Won")
    else:
        print("Invalid Input")
    exit()
print("Welcome to Rock Paper Scissor Game")
print(rps())