# Create a guessing game using while loop
import random

# Generate a random number between 1 and 10
secretNumber = random.randint(1,10)

# Ask user to guess
guess = None
print (" Guess the number between 1 and 10!")

# Loop until the guess is correct
while guess != secretNumber:
    guess = int(input("Input the number:"))

    if guess < secretNumber:
        print("The Number is too low")
    elif guess > secretNumber:
        print("The Number is too high")
    else:
        print("Congratulations")        