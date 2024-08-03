# Factorial is basically number, multiplied with itself till you reach one
# 5! - 5*4*3*2*1

num = int(input("Enter a number "))
factorial = 1  #This variable will be used to store the result of the factorial calculation.
# first check number is pos, neg or zero
if num < 0:
    print("sorry, factorial doesn't exist")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num + 1):               # (For loop) which is going from one till num plus one
        factorial = factorial*i              # range(1,5 + 1)   #1 to 5 + 1   # If num is 5, the loop will run with i taking values 1, 2, 3, 4, 5.
    print("The factorial of",num,"is",factorial)    # After the loop finishes, it prints the final calculated value of factorial.
                                             
'''
# During each iteration of the loop, 
# it multiplies the current value of factorial by i and updates factorial with this new value. 
# This calculates the product of all numbers from 1 to num.
    
Detailed Example:
Iteration 1: factorial = 1 * 1 (factorial is now 1)
Iteration 2: factorial = 1 * 2 (factorial is now 2)
Iteration 3: factorial = 2 * 3 (factorial is now 6)
Iteration 4: factorial = 6 * 4 (factorial is now 24)
Iteration 5: factorial = 24 * 5 (factorial is now 120)
'''
