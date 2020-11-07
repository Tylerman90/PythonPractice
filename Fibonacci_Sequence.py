"""
""
Output the Fibonacci sequence step-by-step.
Fibonacci sequence starts as:
0 1 1 2 3 5 8 13 21 ... in which the first
two numbers are 0 and 1 and each additional
number is the sum of the previous two numbers
""
def fibonacci(v1, v2, run_cnt):
    print(v1, '+', v2, '=', v1+v2)

    if run_cnt <= 1:  # Base case:
                      # Ran for user's number of steps
        pass  # Do nothing
    else:             # Recursive case
        fibonacci(v2, v1+v2, run_cnt-1)


print ('This program outputs the\n'
       'Fibonacci sequence step-by-step,\n'
       'starting after the first 0 and 1.\n')

run_for = int(input('How many steps would you like?'))

fibonacci(0, 1, run_for)
"""

