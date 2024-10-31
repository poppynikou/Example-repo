import numpy as np 

# function which adds two numbers 
def addition(x,y):
    """Adds x and y. 

    :param x: Single number x
    :type x: int or float
    :param y: Single number y 
    :type y: int or float
    :return: Sum of x and y
    :rtype: int or float

    Examples:

    >>> addition(1,3)
    4

    >>> addition('str', 5)
    Traceback (most recent call last):
        ...
    ValueError: Input must be an integer or float

    """

    # Ensure x is int or float
    if type(x) != int or type(x) != float:
        raise ValueError("Input must be an integer or float")

    # Ensure y is int or float
    if type(y) != int or type(y) != float:
        raise ValueError("Input must be an integer or float")

    return x+y 