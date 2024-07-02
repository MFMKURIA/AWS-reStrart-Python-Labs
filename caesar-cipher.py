# Creating a User-Defined Function
# Define a function called getDoubleAlphabet that takes a string argument.
def getDoubleAlphabet(alphabet):
    # Concatenate the given string with itself.
    doubleAlphabet = alphabet + alphabet
    # Return the concatenated string.
    return doubleAlphabet


# Encrypting a Message
# Define a function called getMessage that prompts the user to enter a message.
def getMessage():
    # Use the input function to get a message from the user.
    stringToEncrypt = input("Please enter a message to encrypt: ")
    # Return the message entered by the user.
    return stringToEncrypt


# Getting a Cipher Key
# Define a function called getCipherKey that prompts the user to enter a cipher key.
def getCipherKey():
    # Use the input function to get a cipher key from the user.
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    # Return the cipher key entered by the user.
    return shiftAmount


# Encrypting a Message
# Define a function called encryptMessage that takes three arguments.
def encryptMessage(message, cipherKey, alphabet):
    # Initialize an empty string for the encrypted message.
    encryptedMessage = ""
    # Convert the message to uppercase.
    uppercaseMessage = message.upper()
    # Loop through each character in the uppercase message.
    for currentCharacter in uppercaseMessage:
        # Find the position of the current character in the alphabet.
        position = alphabet.find(currentCharacter)
        # Calculate the new position by adding the cipher key.
        newPosition = position + int(cipherKey)
        # If the current character is in the alphabet, append the new character to the encrypted message.
        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        # If the current character is not in the alphabet, append it unchanged.
        else:
            encryptedMessage += currentCharacter
    # Return the encrypted message.
    return encryptedMessage


# Decrypting a Message
# Define a function called decryptMessage that takes three arguments.
def decryptMessage(message, cipherKey, alphabet):
    # Calculate the decrypt key by multiplying the cipher key by -1.
    decryptKey = -1 * int(cipherKey)
    # Return the encrypted message using the decrypt key.
    return encryptMessage(message, decryptKey, alphabet)


# Creating a Main Function
# Define a function called runCaesarCipherProgram to contain the main logic.
def runCaesarCipherProgram():
    # Define a string variable to contain the English alphabet.
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"Alphabet: {myAlphabet}")
    # Double the alphabet string.
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f"Alphabet2: {myAlphabet2}")
    # Get a message to encrypt from the user.
    myMessage = getMessage()
    print(myMessage)
    # Get a cipher key from the user.
    myCipherKey = getCipherKey()
    print(myCipherKey)
    # Encrypt the message.
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f"Encrypted Message: {myEncryptedMessage}")
    # Decrypt the message.
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f"Decypted Message: {myDecryptedMessage}")


# Calling the Main Function
# Call the runCaesarCipherProgram function to execute the program.
runCaesarCipherProgram()
