# Assigning Variables to the Sequence Elements of Human Insulin
# Python 3.6
# coding: utf-8
# Store the human preproinsulin sequence in a variable called preproInsulin
preproInsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr"
    "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)


# Store the Remaining Sequence Elements of Human Insulin
# Store the remaining sequence elements of human insulin in variables
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Combine Insulin Sequences
insulin = bInsulin + aInsulin

# Printing the sequence of human preproinsulin to console using successive print() commands
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Calculating the molecular weight of insulin
# Creating a list of the amino acid (AA) weights
# Create a Dictionary of Amino Acid Weights
aaWeights = {
    "A": 89.09,
    "C": 121.16,
    "D": 133.10,
    "E": 147.13,
    "F": 165.19,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "K": 146.19,
    "L": 131.17,
    "M": 149.21,
    "N": 132.12,
    "P": 115.13,
    "Q": 146.15,
    "R": 174.20,
    "S": 105.09,
    "T": 119.12,
    "V": 117.15,
    "W": 204.23,
    "Y": 181.19,
}

# Count the Number of Each Amino Acid in the Insulin Sequence
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}

# Calculate the Molecular Weight of Insulin
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights.keys())
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Calculate the Error Percentage
molecularWeightInsulinActual = 5807.63
print(
    "Error percentage: "
    + str(
        (
            (molecularWeightInsulin - molecularWeightInsulinActual)
            / molecularWeightInsulinActual
        )
        * 100
    )
)
