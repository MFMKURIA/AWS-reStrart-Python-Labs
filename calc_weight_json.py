# Import the custom module to handle JSON files
try:
    import json_file_handler  # Try to import the json_file_handler module
except ModuleNotFoundError:
    # Print an error message if the module is not found and exit the program
    print("Error: The 'json_file_handler' module is not found.")
    exit()

# Retrieve the JSON data from the insulin.json file
data = json_file_handler.read_json_file(
    "insulin.json"
)  # Call the read_json_file function

# Check if data is retrieved successfully
if data:
    # Accessing specific insulin molecule sequences
    b_insulin = data["molecules"][
        "bInsulin"
    ]  # Retrieve the bInsulin sequence from JSON data
    a_insulin = data["molecules"][
        "aInsulin"
    ]  # Retrieve the aInsulin sequence from JSON data
    # Combine the b and a insulin sequences
    insulin = b_insulin + a_insulin  # Concatenate bInsulin and aInsulin sequences

    # Accessing the actual molecular weight of insulin
    molecular_weight_insulin_actual = data[
        "molecularWeightInsulinActual"
    ]  # Retrieve the actual molecular weight
    print("bInsulin: " + b_insulin)  # Print the bInsulin sequence
    print("aInsulin: " + a_insulin)  # Print the aInsulin sequence
    print(
        "molecularWeightInsulinActual: " + str(molecular_weight_insulin_actual)
    )  # Print the actual molecular weight

    # Getting a list of the amino acid weights
    aa_weights = data["weights"]  # Retrieve the dictionary of amino acid weights

    # Counting the number of each amino acid in the insulin sequence
    aa_count_insulin = {x: float(insulin.upper().count(x)) for x in aa_weights.keys()}
    # Create a dictionary where the keys are amino acids and the values are their counts in the insulin sequence

    # Calculating the total molecular weight of insulin based on amino acid counts and weights
    molecular_weight_insulin = sum(
        {x: (aa_count_insulin[x] * aa_weights[x]) for x in aa_weights.keys()}.values()
    )
    # Multiply the count of each amino acid by its weight and sum the results to get the total molecular weight

    # Printing the calculated rough molecular weight of insulin and percent error
    print(
        "The rough molecular weight of insulin: " + str(molecular_weight_insulin)
    )  # Print the calculated molecular weight
    print(
        "Percent error: "
        + str(
            (
                (molecular_weight_insulin - molecular_weight_insulin_actual)
                / molecular_weight_insulin_actual
            )
            * 100
        )
    )
    # Calculate the percent error between the actual and calculated molecular weights and print it
else:
    # Print an error message if data retrieval fails
    print("Error. Exiting program")  # Print an error message and exit the program
