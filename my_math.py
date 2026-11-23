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

#Andrel Sheppard functions

"""
function name: pow
purpose: Returns the result of raising a number x to
the power of y. The function validates that both
inputs are numbers and rejects invalid inputs.
It also prevents division by zero when x is zero
and y is negative.
parameters:
x (int or float): The base number.
y (int or float): The exponent.
return value(s):
(int or float): The result of x raised to the power of y.

"""

def pow(x, y):
    if not isinstance(x, (int, float)) or isinstance(x, bool):
        raise TypeError("The base must be a number.")

    if not isinstance(y, (int, float)) or isinstance(y, bool):
        raise TypeError("The exponent must be a number.")

    if x == 0 and y < 0:
        raise ValueError("Zero cannot have a negative exponent.")

    return x ** y


"""

function name: area_of_circle(r)
purpose:Calculates the area of a circle using the formula π × r². 
The function validates that the input is a number (booleans and strings are rejected) 
and that the radius is not negative.
Parameters: r (int or float): The non-negative radius of the circle.
Return value(s): (float): The area of the circle.

"""

from math import pi

def area_of_circle(r):
    """
    Calculates the area of a circle.

    Parameters:
        r (int or float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """

    if not isinstance(r, (int, float)) or isinstance(r, bool):
        raise TypeError("Radius must be a number.")

    if r < 0:
        raise ValueError("Radius cannot be negative.")

   
    return pi * pow(r, 2)






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


"""

function name: sqrt
purpose: Computes the square root of a non-negative number using Newton's method,
without using the math module. The function validates that the input is a number
(booleans and strings are rejected) and that it is not negative.
parameters: x (int or float): A non-negative number.
return value(s): (float): The square root of x.

"""

def sqrt(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError("sqrt(x) requires a number")
    if x < 0:
        raise ValueError("x must be non-negative")

    guess = x
    if x == 0:
        return 0.0
    for i in range(50):
        guess = (guess + x/guess)/2.0

    return guess


