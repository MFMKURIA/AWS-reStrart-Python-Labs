# Printing the Game Rules
print("Welcome to Guess the Number!")  # Display a welcome message
print(
    "The rules are simple. I will think of a number, and you will try to guess it."
)  # Explain the rules


# Importing random and Writing a while Loop:
import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 10:
number = random.randint(1, 10)  # Generate a random number between 1 and 10

# Track whether the user guessed the number correctly:
isGuessRight = False  # Initialize a variable to track the guessing status

# Create the while loop:
while isGuessRight != True:  # Loop until the user guesses the correct number
    guess = input("Guess a number between 1 and 10: ")  # Prompt the user for a guess
    if int(guess) == number:  # Check if the guess is correct
        print(
            "You guessed {}. That is correct! You win!".format(guess)
        )  # Inform the user they guessed correctly
        isGuessRight = True  # Set the flag to True to exit the loop
    else:
        print(
            "You guessed {}. Sorry, that isn’t it. Try again.".format(guess)
        )  # Inform the user their guess was incorrect
