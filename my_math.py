# my_math.py

"""

Please provide the description of the function.
function name: fibonacci 
purpose: Computes the nth number in the Fibonacci sequence using an iterative approach. 
The function also validates the input to ensure it is a non-negative integer.
parameters: n (int): A non-negative integer representing 
the position in the Fibonacci sequence.
return value(s): (int): The nth Fibonacci number.

"""

def fibonacci(n):

    if not isinstance(n, int):
        raise TypeError("fibonacci(n) requires an integer n")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



"""

Please provide the description of the function.
function name: mean
purpose: Calculates the average (arithmetic mean) of a collection of numeric values. 
The function validates that all elements are numbers and ensures the input is not empty.
parameters: A collection (e.g., list, tuple) of numeric values (integers or floats).
return value(s): (float): The average of the input values
"""

def mean(values):

    total = 0.0
    count = 0

    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("mean() expects all elements to be numbers")
        total += float(v)
        count += 1

    if count == 0:
        raise ValueError("mean() of empty data")

    return total / count

#power function






#factorial function







#Larry Marin Functions
"""

function name: divisors
purpose: Returns all positive divisors of a positive integer in ascending order.
The function validates that the input is a positive integer (0, negative numbers,
decimals, booleans, and strings are rejected).
parameters: n (int): A positive integer.
return value(s): (list): A sorted list of all positive divisors of n.

"""

def divisors(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("divisors(n) requires an integer n")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    numList = []
    i = 1
    while i*i <= n:
        if n%i == 0:
            numList.append(i)
            if n//i != i:
                numList.append(n//i)
        i+=1
    numList.sort()
    return numList

def sqrt(x):
    guess = x
    if x == 0:
        return 0.0
    for i in range(50):
        guess = (guess + x/guess)/2.0

    return guess
