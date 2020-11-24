"""
In mathematics, Pascal's triangle is a triangular array of the binomial
coefficients expressed with formula (n k) = n!/(n-k)!, where n denotes a
row of the triangle, and k is a position of a term in the row.

Test.assert_equals(pascals_triangle(1), [1],"1 level triangle incorrect");
Test.assert_equals(pascals_triangle(2), [1,1,1],"2 level triangle incorrect");
Test.assert_equals(pascals_triangle(3), [1,1,1,1,2,1],"3 level triangle incorrect");
"""

import math


def pascals_triangle(n):
    triangle = []

    def C(n, x):
        return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

    for row in range(0, n):
        for col in range(0, row+1):
            triangle.append(int(C(row, col)))

    return triangle


print(pascals_triangle(4))
