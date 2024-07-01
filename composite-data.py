# Importing Modules
import csv  # Importing the csv module to work with CSV files
import copy  # Importing the copy module to create deep copies of objects

# Defining the Dictionary
myVehicle = {
    "vin": "<empty>",  # Vehicle Identification Number, initially empty
    "make": "<empty>",  # Manufacturer of the vehicle, initially empty
    "model": "<empty>",  # Model of the vehicle, initially empty
    "year": 0,  # Year of manufacture, initially 0
    "range": 0,  # Range of the vehicle, initially 0
    "topSpeed": 0,  # Top speed of the vehicle, initially 0
    "zeroSixty": 0.0,  # Time to accelerate from 0 to 60 mph, initially 0.0
    "mileage": 0,  # Mileage of the vehicle, initially 0
}

# Iterating Over the Dictionary
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Defining the List for Car Inventory
myInventoryList = []  # Creating an empty list to hold the inventory of vehicles

# Reading and Copying Data from the CSV File
with open("car_fleet.csv") as csvFile:  # Open the CSV file for reading
    csvReader = csv.reader(
        csvFile, delimiter=","
    )  # Create a CSV reader object to read the file
    lineCount = 0  # Initialize a line counter

    for row in csvReader:  # Iterate over each row in the CSV file
        if lineCount == 0:  # Check if it is the first row (header)
            print(f'Column names are: {", ".join(row)}')  # Print the column names
            lineCount += 1  # Increment the line counter
        else:
            # Print each field in the row with its corresponding value
            print(
                f"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}"
            )

            currentVehicle = copy.deepcopy(
                myVehicle
            )  # Create a deep copy of the myVehicle dictionary

            # Assign values from the CSV row to the corresponding keys in the dictionary
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            myInventoryList.append(
                currentVehicle
            )  # Add the populated dictionary to the inventory list

            lineCount += 1  # Increment the line counter

    print(f"Processed {lineCount} lines.")  # Print the total number of lines processed

# Printing the Car Inventory
for myCarProperties in myInventoryList:  # Iterate over each car in the inventory list
    for (
        key,
        value,
    ) in (
        myCarProperties.items()
    ):  # Iterate over each key-value pair in the car dictionary
        print(
            "{} : {}".format(key, value)
        )  # Print each key and its corresponding value
    print("-----")  # Print a separator between cars
