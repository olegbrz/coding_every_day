"""Alright, detective, one of our colleagues successfully observed our target
person, Robby the robber. We followed him to a secret warehouse, where we
assume to find all the stolen stuff. The door to this warehouse is secured by
an electronic combination lock. Unfortunately our spy isn't sure about the PIN
he saw, when Robby entered it.

The keypad has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits
he saw could actually be another adjacent digit (horizontally or vertically,
but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And
instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited
amount of wrong PINs, they never finally lock the system or sound the alarm.
That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering
the adjacent digits

Can you help us to find all those variations? It would be nice to have a
function, that returns an array (or a list in Java and C#) of all variations
for an observed PIN with a length of 1 to 8 digits. We could name the function
getPINs (get_pins in python, GetPINs in C#). But please note that all PINs,
the observed one and also the results, must be strings, because of potentially
leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!
"""

import itertools
import numpy as np


def get_pins(observed):

    def adjacents(digit):
        """Function that gets the digit of the numpad as input
        and outputs all its adjacent digits"""

        digit = int(digit)

        numpad = np.matrix([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [-1, 0, -1]])

        numpad = np.pad(numpad, (1, 1), 'constant', constant_values=-1)

        pos_map = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1),
                   6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
        x, y = pos_map[digit]

        adjacents = [numpad[x+1, y+1],                 # The digit itself
                     numpad[x, y+1], numpad[x+2, y+1],  # Left and right
                     numpad[x+1, y], numpad[x+1, y+2]]  # Up and down

        # Filter -1 values
        adjacents = [x for x in adjacents if x != -1]
        return adjacents

    possibilities = [adjacents(x) for x in observed]

    # Cartesian product of all positions
    combinations = []
    for product in list(itertools.product(*possibilities)):
        combinations.append(''.join([str(digit) for digit in product]))

    return combinations
