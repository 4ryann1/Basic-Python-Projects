# Here are some basic Python projects perfect for beginners to practice fundamental programming concepts.
# Number Guessing Game 🔢
# A fun game where the computer thinks of a random number, and the user has to guess it.
# Description: The program generates a secret random number within a range (e.g., 1 to 100).
# The user enters guesses, and the program tells them if their guess is too high, too low, or correct.
# You can also add a limit on the number of guesses.
# Concepts Covered: random module, input() and print() functions, while loops, if/elif/else statements,
# and converting strings to integers.
# Next Step: Add difficulty levels that change the range of numbers (e.g., 1-50 for easy, 1-100 for hard).

import random

def checker1():
    number = random.randint(1,50)
    attempt=0
    while True:
        try:
            guess=int(input("Guess a Random Integer: "))
            attempt+=1
            if guess > number:
                print("Too High")
            elif guess < number:
                print("Too Low")
            else:
                print("Correct")
        except ValueError:
            print("Incorrect value")
def checker2():
    number = random.randint(1,100)
    attempt=0
    while True:
        try:
            guess=int(input("Guess a Random Integer: "))
            attempt+=1
            if guess > number:
                print("Too High")
            elif guess < number:
                print("Too Low")
            else:
                print("Correct")
        except ValueError:
            print("Incorrect value")
print("*********************************************WELCOME TO BASIC NUMBER GAME******************************************************************")
print("Welcome to Number Guessing Game")

diff = int(input('''Enter 1 for Easy
Enter 2 for Hard:
Enter a Number'''))
if diff == 1:
    checker1()
elif diff == 2:
    checker2()
else:
    print("Incorrect input")
print(f"checker{diff}()")