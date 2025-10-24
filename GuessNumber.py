# GuessNumber.py - This program allows a user to guess a number between 1 and 10.
# Input:  User guesses numbers until they get it right.
# Output: Tells users if they are right or wrong.

from random import randint

number = randint(1, 10) # Generate random number.

# Prime the loop.
keepGoing = input("Do you want to guess a number? Enter Y or N: ")

# Validate input.
while keepGoing not in ("Y", "N"):
    keepGoing = input("Do you want to guess a number? Enter Y or N: ")

# Enter loop if they want to play.
while keepGoing == "Y":
    # Get user's guess.
    stringNumber = input("I'm thinking of a number...\nTry to guess by entering a number between 1 and 10. ")
    userNumber = int(stringNumber)
    # Validate input.
    while not stringNumber.isdigit() or not (1 <= int(stringNumber) <= 10):
        stringNumber = input("Number must be in the range of 1 to 10: Please try again: ")

    # Test to see if the user guessed correctly.
    if userNumber == number:
        keepGoing = "N"
        print("You are a genius. That's correct!")

    else:
        keepGoing = input("That's not correct. Do you want to guess again? Enter Y or N: ")

        # Validate input.
        while keepGoing not in ("Y", "N"):
            keepGoing = input("Do you want to guess a number? Enter Y or N: ")

# End of while loop.

print("Thanks for playing!")
