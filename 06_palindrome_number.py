# "12321" or "4321234" thi is called palindrome number

n=int(input("Enter the number: "))
temp=n
rev=0
while(n>0):
    dig=n%0
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("The number is not palindrome!")

'''
Modulo Operator (%): This operator returns the remainder of division. It's used here to extract the last digit of the number.
Integer Division (//): This operator performs division and returns the integer part of the quotient. It's used to remove the last digit from the number.
Reversing Logic: By shifting the rev variable by multiplying it by 10 and adding the last digit dig, we effectively reverse the number step by step.
'''
