# Name:
# Login:
# TA:
# Section:
# Q1.

def stone_age():
    """Returns the year in which Steven and Eric took CS 61A."""
    return  _____

# Q2.

def favorite_player():
    """Returns Steven's favorite basketball player."""
    return  '_____'

# Q3.

def favorite_number():
    """Returns Eric's favorite number."""
    return  _____

# Q4.

from operator import add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = _____
    else:
        op = _____
    return op(a, b)

# Q5.

#def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"

def two_of_three(a,b,c):
    first = max(a,b,c)
    second = min(max(a,b), max(a,c), max(b,c))
    return first * first + second * second   

# Q6.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"

def t():
    "*** YOUR CODE HERE ***"

def f():
    "*** YOUR CODE HERE ***"

# Q7.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

