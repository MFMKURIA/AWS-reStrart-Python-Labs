# Creating a mixed-type list
# Define a list with different types:
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Use a for loop statement to traverse the list and print the data type for each item
# Use a for loop to iterate over each item in the list myMixedTypeList
for item in myMixedTypeList:
    # Print each item and its data type
    # {} placeholders are replaced by the item and its type
    # .format(item, type(item)) method inserts item and its type into the placeholders
    print("{} is of the data type {}".format(item, type(item)))

# Define a list named myMixedTypeList containing elements of different data types
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
