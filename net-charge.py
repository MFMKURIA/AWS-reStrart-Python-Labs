# Assigning Variables, Lists, and Dictionaries
# Python3.6
# Coding: utf-8

# Store the human preproinsulin sequence in a variable called preproinsulin:
# This sequence is the initial form of insulin before it is processed into its active form.
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
# These variables represent different parts of the insulin molecule.
lsInsulin = "malwmrllpllallalwgpdpaaa"  # The signal sequence that is removed in the mature form.
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  # The B chain of insulin.
aInsulin = "giveqcctsicslyqlenycn"  # The A chain of insulin.
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  # The C-peptide that is removed in the mature form.

# Combine the B and A chains to get the full insulin molecule.
insulin = bInsulin + aInsulin

# Create a dictionary to store the pKa values of the amino acids that contribute to the net charge.
# pKa values indicate the strength of an acid; the lower the pKa, the stronger the acid.
pKR = {
    "y": 10.07,  # Tyrosine
    "c": 8.18,  # Cysteine
    "k": 10.53,  # Lysine
    "h": 6.00,  # Histidine
    "r": 12.48,  # Arginine
    "d": 3.65,  # Aspartic acid
    "e": 4.25,  # Glutamic acid
}


# Using count() to Count the Numbers of Each Amino Acid
# Use the count() method to count the number of each amino acid in the insulin sequence.
# The count() method returns the number of occurrences of a substring in a string.

# Here, float() is used to ensure that the count is treated as a float for calculations.
# This line of code creates a dictionary that maps each amino acid to its count in the insulin sequence.
seqCount = {x: float(insulin.count(x)) for x in ["y", "c", "k", "h", "r", "d", "e"]}
# The dictionary comprehension iterates over a list of amino acids and counts their occurrences in the insulin sequence.
# The resulting dictionary looks like this: {'y': count_of_y, 'c': count_of_c, ...}

# Writing the Net Charge Formula
# Initialize the pH variable to zero. The pH scale typically ranges from 0 to 14.
pH = 0

# Create a while loop that will run as long as pH is less than or equal to 14.
while pH <= 14:
    # Calculate the net charge of the insulin molecule at the current pH.
    # This formula sums the contributions of the positively and negatively charged amino acids.
    netCharge = (
        +(
            sum(
                {
                    x: ((seqCount[x] * (10 ** pKR[x])) / ((10**pH) + (10 ** pKR[x])))
                    for x in ["k", "h", "r"]
                }.values()
            )
        )
        # For positively charged amino acids (K, H, R), this part calculates their contributions to the net charge.
        - (
            sum(
                {
                    x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10 ** pKR[x])))
                    for x in ["y", "c", "d", "e"]
                }.values()
            )
        )
        # For negatively charged amino acids (Y, C, D, E), this part calculates their contributions to the net charge.
    )

    # Print the current pH and the calculated net charge.
    # '{0:.2f}'.format(pH) formats the pH value to two decimal places for readability.
    print("{0:.2f}".format(pH), netCharge)

    # Increment the pH value by 1 to move to the next pH level.
    pH += 1
