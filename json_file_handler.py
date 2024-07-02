# Import the JSON module to work with JSON data
import json


# Define a function to read a JSON file and return its content
def read_json_file(file_name):
    data = ""  # Initialize an empty string to store the data
    try:
        # Open the JSON file for reading with utf-8 encoding
        with open(file_name, "r", encoding="utf-8") as json_file:
            # Load and parse the JSON content
            data = json.load(json_file)
            print("File read successfully.")
    except IOError:
        # Print an error message if the file cannot be read
        print(f"Could not read file: {file_name}")
    except json.JSONDecodeError:
        # Print an error message if the file is not valid JSON
        print(f"Error decoding JSON from file: {file_name}")
    return data  # Return the parsed JSON data
