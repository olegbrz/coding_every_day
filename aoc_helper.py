from sys import argv
from requests import get
from json import load
from typing import List


def get_input() -> List[str]:
    """get_input gets the AoC input of the day based on the name of the file,
    which should have this format: 000_010120_AOCx.py, where x is the day of
    the challenge.

    Returns:
        List[str]: list of strings from the input.
    """
    with open('aoc_cookie.json') as c:
        data = load(c)

    day = argv[0].split('/')[-1].split('.')[0].split('AOC')[-1]
    # Load the cookie from .json
    headers = {'cookie': data['cookie']}
    # GET to the challenge
    r = get(f'https://adventofcode.com/2020/day/{day}/input', headers=headers)
    return r.text.split('\n')[:-1]
