#Random guessing game

import random 

print("----------- Random Number Guessing Game -------------------------")

print("Enter your Range (Lowest - Highest)")

lowest = int(input("Enter The Lowest number in range: "))
highest = int(input("Enter the Highest number in range: "))

random = random.randint(lowest, highest)
isRunning = True

guess = 0
score = 0
print()
print(f"Enter a number between {lowest} and {highest}")

while isRunning:
    print()
    guess = input("Enter a number:")

    if guess.isdigit():
        guess = int(guess)
        score += 1
        if guess < lowest or guess > highest:
            print("Number out or range!")
            print(f"Enter a number between {lowest} and {highest}")
        elif guess < random:
            print("Too Low! Try Again!")
        elif guess > random:
            print("Too High! Try Again!")
        else:
            print("----------------------------------")
            print(f"Correct! The Answer is {random}")
            print(f"Took you {score} Guesses")
            print("----------------------------------")
            isRunning = False
    
    else:
        print("Invalid Guess!")
        print(f"Enter a number between {lowest} and {highest}")