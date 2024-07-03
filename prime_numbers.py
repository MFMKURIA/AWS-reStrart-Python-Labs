# Connect to the Linux Host EC2 Instance
# Create and Navigate to Your Working Directory
# cd~
# Write the Python Script
# prime_numbers.py


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# List to store prime numbers
prime_numbers = []

# Loop through numbers from 1 to 250 and check for primes
for num in range(1, 251):
    if is_prime(num):
        prime_numbers.append(num)

# File path to store results
file_path = "D:\AWS reStart Python\AWS reStrart Python Labs\results.txt"

# Write prime numbers to the results file
with open(file_path, "w") as file:
    for prime in prime_numbers:
        file.write(str(prime) + "\n")

print(f"Prime numbers between 1 and 250 written to {file_path}")


# Save the prime_numbers.py script and make it executable:
# chmod +x prime_numbers.py
# Run the script using Python 3:
# python3 prime_numbers.py
# cat results.txt
