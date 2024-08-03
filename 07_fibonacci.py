# Find the element from #fibonacci - 0 1 1 2 3 5 8
# let's say it's 5 - so it will be 3

n=int(input("What is the number: "))
a = 0
b = 1
if n < 0:           # let's input 5 is less than 0 - FALSE
    print("incorrect input")
elif n == 0:        # let's input 5 is equal to 0 - if True print A or FALSE
    print(a)
elif n == 1:        # let's input 5 is equal to 1 - print A or FALSE
    print(a)
else:
    for i in range(2,n):  #
        c = a + b
        a = b      # Updates a to the current value of b. This effectively shifts a to the next Fibonacci number in the sequence.
        b = c      # Updates b to the current value of c.
    print(b)


'''
Loop Begins: The loop runs for i values 2, 3, and 4.

Iteration 1 (i=2):

c = a + b = 0 + 1 = 1
a = b = 1
b = c = 1
Fibonacci Sequence So Far: 0, 1, 1

Iteration 2 (i=3):

c = a + b = 1 + 1 = 2
a = b = 1
b = c = 2
Fibonacci Sequence So Far: 0, 1, 1, 2
Iteration 3 (i=4):

c = a + b = 1 + 2 = 3
a = b = 2
b = c = 3
Fibonacci Sequence So Far: 0, 1, 1, 2, 3

Key Concepts
Fibonacci Sequence: Each number is the sum of the two preceding ones. It starts with 0 and 1, and every subsequent number is formed by adding the previous two.
Iterative Calculation: The loop iteratively calculates each Fibonacci number up to the specified position.
Initial Values: The sequence begins with a = 0 and b = 1, corresponding to the first two numbers of the Fibonacci series.
'''