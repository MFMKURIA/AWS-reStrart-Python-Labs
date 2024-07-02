# Creating the Main Program
# Import the jsonFileHandler module to access the readJsonFile function.
import json_File_Handler

# Retrieve the JSON data from the insulin.json file.
data = json_File_Handler.readJsonFile("files/insulin.json")

# Check if data is retrieved successfully.
if data != "":
    # Accessing specific insulin molecule sequences.
    bInsulin = data["molecules"]["bInsulin"]
    aInsulin = data["molecules"]["aInsulin"]
    insulin = bInsulin + aInsulin

    # Accessing the actual molecular weight of insulin.
    molecularWeightInsulinActual = data["molecularWeightInsulinActual"]
    print("bInsulin: " + bInsulin)
    print("aInsulin: " + aInsulin)
    print("molecularWeightInsulinActual: " + str(molecularWeightInsulinActual))

    # Calculating the molecular weight of insulin.
    # Getting a list of the amino acid weights.
    aaWeights = data["weights"]

    # Counting the number of each amino acid in the insulin sequence.
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}

    # Calculating the total molecular weight of insulin based on amino acid counts and weights.
    molecularWeightInsulin = sum(
        {x: (aaCountInsulin[x] * aaWeights[x]) for x in aaWeights.keys()}.values()
    )

    # Printing the calculated rough molecular weight of insulin and percent error.
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print(
        "Percent error: "
        + str(
            (
                (molecularWeightInsulin - molecularWeightInsulinActual)
                / molecularWeightInsulinActual
            )
            * 100
        )
    )
else:
    print("Error. Exiting program")
