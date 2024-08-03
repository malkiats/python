# you have 123
# make it 321

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig      # If rev was 0 and dig is 3, then rev becomes 0 * 10 + 3 = 3.
    n=n//10             # It removes the last digit from n by performing integer division by 10.
                        # Example: For n = 123, n becomes 123 // 10 = 12.
print("Reverse of the number:",rev)


# It calculates the last digit of the current number n by finding the remainder when n is divided by 10. 
# This last digit is stored in the variable dig.
# Example: For n = 123, dig will be 3 because 123 % 10 is 3.

'''
Iteration 1:

n = 123
dig = 123 % 10 = 3
rev = 0 * 10 + 3 = 3
n = 123 // 10 = 12
Iteration 2:

n = 12
dig = 12 % 10 = 2
rev = 3 * 10 + 2 = 32
n = 12 // 10 = 1
Iteration 3:

n = 1
dig = 1 % 10 = 1
rev = 32 * 10 + 1 = 321
n = 1 // 10 = 0

Modulo Operator (%): This operator returns the remainder of division. It's used here to extract the last digit of the number.
Integer Division (//): This operator performs division and returns the integer part of the quotient. It's used to remove the last digit from the number.
Reversing Logic: By shifting the rev variable by multiplying it by 10 and adding the last digit dig, we effectively reverse the number step by step.

'''