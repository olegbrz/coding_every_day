"""Welcome.

In this kata you are required to, given a string, replace every letter with its
position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""

import string
alphabet = list(string.ascii_lowercase)


def alphabet_position(text):
    return ' '.join([str(alphabet.index(letter.lower())+1) for letter in
                     ''.join(text.split()) if letter.lower() in alphabet])
