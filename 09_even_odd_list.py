def separate_even_odd(numbers):
    """Separate the even and odd numbers from a list."""
    even_numbers = []  # List to store even numbers
    odd_numbers = []   # List to store odd numbers

    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            even_numbers.append(number)
        else:                # Otherwise, it's odd
            odd_numbers.append(number)

    return even_numbers, odd_numbers

def main():
    # Ask the user to input a list of numbers
    input_string = input("Enter a list of numbers without spaces (e.g., 123456789): ")

    # Convert the input string into a list of integers
    numbers = [int(char) for char in input_string]

    # Get the even and odd numbers using the separate_even_odd function
    even_numbers, odd_numbers = separate_even_odd(numbers)

    # Print the results
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

if __name__ == "__main__":
    main()
