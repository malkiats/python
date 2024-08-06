def separate_even_odd(numbers):         # numbers (parameters representing a list of numbers): Any -> tuple[list, list]
    """Separate the even and odd numbers from a list."""
    even_numbers = []  # List to store even numbers
    odd_numbers = []   # List to store odd numbers

    for number in numbers:   # This is a for loop that iterates over each number in the numbers list.
        if number % 2 == 0:  # Check if the number is even - The % operator calculates the remainder when number is divided by 2.
            even_numbers.append(number)   # it is added to the even_numbers list using the append() method.
        else:                # Otherwise, it's odd
            odd_numbers.append(number)

    return even_numbers, odd_numbers  # After the loop finishes, the function returns two lists: even_numbers and odd_numbers.

def main():  # contains the main logic of the script.
    # Ask the user to input a list of numbers
    input_string = input("Enter a list of numbers without spaces (e.g., 123456789): ")

    # Convert the input string into a list of integers
    numbers = [int(char) for char in input_string] # This line uses a list comprehension to convert each character in input_string into an integer.

    # Get the even and odd numbers using the separate_even_odd function
    even_numbers, odd_numbers = separate_even_odd(numbers)

    # Print the results
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

if __name__ == "__main__":
    main()

'''
int(char):
Converts the character char to an integer.

[int(char) for char in input_string]:
Constructs a list of integers from the characters in the input string.
Example:

If input_string is '123456789', the list comprehension results in [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''

'''
Script Execution

if __name__ == "__main__":
    main()

Conditional Check:
if __name__ == "__main__":

This line checks if the script is being run directly (not imported as a module).

__name__ is a special variable in Python that holds the name of the module being executed.

If the script is executed directly, __name__ is set to "__main__".
'''
