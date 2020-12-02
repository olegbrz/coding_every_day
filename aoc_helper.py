from sys import argv
from requests import get
from json import load


def get_input():
    with open('aoc_cookie.json') as c:
        data = load(c)

    day = argv[0].split('/')[-1].split('.')[0].split('AOC')[-1]
    # Load the cookie from .json
    headers = {'cookie': data['cookie']}
    # GET to the challenge
    r = get(f'https://adventofcode.com/2020/day/{day}/input', headers=headers)
    return r.text.split('\n')[:-1]
