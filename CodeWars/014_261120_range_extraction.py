"""A format for expressing an ordered list of integers is to use a comma
separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end
integer in the range by a dash, '-'. The range includes all integers in the
interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order
and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""


def solution(l):

    def check_last(r):
        if len(r[-1]) == 2:
            for _ in r[-1]:
                r.append([r[-1].pop()])

    # Group by ranges and check if len is not 2
    ranges = []
    for n in range(len(l)):
        if not ranges:
            ranges.append([l[n]])
        else:
            if l[n] - ranges[-1][-1] == 1:
                ranges[-1].append(l[n])
            else:
                check_last(ranges)
                ranges.append([l[n]])
    check_last(ranges)

    # Build return string from ranges list
    for i in range(len(ranges)):
        if len(ranges[i]) == 1:
            ranges[i] = str(ranges[i][0])
        else:
            ranges[i] = f'{ranges[i][0]}-{ranges[i][-1]}'

    return ','.join(ranges)
