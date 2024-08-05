# Ask the user to input a list of numbers
input_string = input("Enter a list of numbers without spaces (e.g., 123456789): ")

# Convert the input string into a list of integers
numbers = [int(char) for char in input_string]

# Initialize lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the list of numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)  # Append to even_numbers if the number is even
    else:
        odd_numbers.append(number)   # Append to odd_numbers if the number is odd

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)