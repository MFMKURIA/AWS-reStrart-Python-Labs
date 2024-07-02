# Retrieving the protein sequence of human preproinsulin
# Search for human insulin protein
# Copy the insulin sequence
# create a txt file with the sequence
# prepoinsulin-seq.txt
# Cleaning preproinsulin-seq.txt programmatically

# Open the file for reading
with open("preproinsulin-seq.txt", "r") as file:
    # Read the lines from the file
    lines = file.readlines()

# Initialize an empty string to hold the cleaned sequence
cleaned_sequence = ""

# Loop through each line in the file
for line in lines:
    # Skip lines that contain 'ORIGIN' or '//'
    if "ORIGIN" in line or "//" in line:
        continue
    # Remove the line numbers and spaces
    cleaned_sequence += line[10:].strip()

# Print the cleaned sequence
print(cleaned_sequence)

# Save the cleaned sequence to a new file
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(cleaned_sequence)

#Obtaining the protein sequence of human insulin
# Define the cleaned preproinsulin sequence
preproinsulin_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealy lvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Extract the parts of the sequence
lsinsulin_seq = preproinsulin_sequence[:24]  # Amino acids 1-24
binsulin_seq = preproinsulin_sequence[24:54]  # Amino acids 25-54
cinsulin_seq = preproinsulin_sequence[54:89]  # Amino acids 55-89
ainsulin_seq = preproinsulin_sequence[89:]  # Amino acids 90-110

# Save the sequences to their respective files
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin_seq)

with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin_seq)

with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin_seq)

with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin_seq)
