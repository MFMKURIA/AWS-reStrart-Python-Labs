# part 1
# This line of code assigns a string to the variable myString
myString = "This is a string."

# This line of code prints the value of myString to the console
print(myString)

# part 2
# This line of code prints the type of myString, which is <class 'str'>
print(type(myString))

# This line of code concatenates strings and prints the result
# It uses the str() function to convert the type information to a string for concatenation
print(myString + " is of the data type " + str(type(myString)))

# part 3
# This line of code assigns the string "water" to the variable firstString
firstString = "water"

# This line of code assigns the string "fall" to the variable secondString
secondString = "fall"

# This line of code concatenates firstString and secondString and assigns the result to thirdString
thirdString = firstString + secondString

# This line of code prints the value of thirdString to the console
print(thirdString)

# part 4
# This line of code prompts the user to enter their name and assigns the input to the variable name
name = input("What is your name? ")

# This line of code prints the value of name to the console
print(name)

# part 5
# This line of code prompts the user to enter their favorite color and assigns the input to the variable color
color = input("What is your favorite color? ")

# This line of code prompts the user to enter their favorite animal and assigns the input to the variable animal
animal = input("What is your favorite animal? ")

# This line of code formats and prints a string using the name, color, and animal variables
# The {} placeholders in the string are replaced by the values of name, color, and animal in that order
print("{}, you like a {} {}!".format(name, color, animal))
