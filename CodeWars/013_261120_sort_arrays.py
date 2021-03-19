"""This time the input is a sequence of course-ids that are formatted in the
following way:

name-yymm

The return of the function shall first be sorted by yymm, then by the name
(which varies in length).
"""


def sort_me(x): return sorted(
    x, key=lambda x: (x.split('-')[1], x.split('-')[0]))
