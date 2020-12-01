""" --- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you
a starfish coin they had left over from a past vacation. They offer you a
second one if you can find three numbers in your expense report that meet the
same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?
"""

from requests import get
from json import load

with open('021_cookie.json') as c:
    data = load(c)

# Load the cookie from .json
headers = {'cookie': data['cookie']}
# GET to the challenge
r = get('https://adventofcode.com/2020/day/1/input', headers=headers)


def search(nums):
    """search Iterates over a list and compares all permutations
    of the list to find two numbers than sum 2020.
    Args:
            nums ([int]): [list of numbers to search trough]

    Returns:
            [int]: [the product of the two found numbers]
    """

    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3


# Transform to int the list of numbers
data = [int(n) for n in r.text.split('\n')[:-1]]

print(f'Result: {search(data)}')
