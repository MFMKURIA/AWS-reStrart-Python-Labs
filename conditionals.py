# Edit the Python Script to Ship Packages
# Working with the else Statement
# Ask the user if they need to ship a package
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Check if the user replied with 'yes'
if userReply == "yes":
    # If yes, print a message indicating help to ship the package
    print("We can help you ship that package!")
else:
    # If no, print a message indicating to come back when they need to ship a package
    print("Please come back when you need to ship a package. Thank you.")

# Working with the elif Statement
# Ask the user if they would like to buy stamps, buy an envelope, or make a copy
userReply = input(
    "Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) "
)

# Check if the user wants to buy stamps
if userReply == "stamps":
    # If yes, print a message indicating the availability of many stamp designs
    print("We have many stamp designs to choose from.")
# Check if the user wants to buy an envelope
elif userReply == "envelope":
    # If yes, print a message indicating the availability of many envelope sizes
    print("We have many envelope sizes to choose from.")
# Check if the user wants to make a copy
elif userReply == "copy":
    # If yes, ask how many copies they would like
    copies = input("How many copies would you like? (Enter a number) ")
    # Print the number of copies requested
    print("Here are {} copies.".format(copies))
else:
    # If none of the above conditions are met, print a thank you message
    print("Thank you, please come again.")
