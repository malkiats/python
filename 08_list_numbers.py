num = int(input("Enter a number: "))
if num < 0:
    print("Sorry, list doesn't exist")
else:
    result = ""  # Initialize an empty string to store the concatenated numbers
    for i in range(1,num + 1):
        result += str(i)  # Convert the number to a string and append it to the result
    print("The list of",num,"is",result)

# += str(i)
# link (things) together in a chain or series.