"""This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function
represents the right operand
Division should be integer division. For example, this should return 2, not
2.666666...:

eight(divided_by(three()))
"""


def zero(operator=lambda x: x): return operator(0)
def one(operator=lambda x: x): return operator(1)
def two(operator=lambda x: x): return operator(2)
def three(operator=lambda x: x): return operator(3)
def four(operator=lambda x: x): return operator(4)
def five(operator=lambda x: x): return operator(5)
def six(operator=lambda x: x): return operator(6)
def seven(operator=lambda x: x): return operator(7)
def eight(operator=lambda x: x): return operator(8)
def nine(operator=lambda x: x): return operator(9)


def plus(addend2): return lambda addend1: addend1 + addend2
def minus(subtrahend): return lambda minuend: minuend - subtrahend
def times(factor2): return lambda factor1: factor1 * factor2
def divided_by(divisor): return lambda dividend: dividend // divisor
