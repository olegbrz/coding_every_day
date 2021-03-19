"""A food delivery truck carrying boxes of delicious sausages has arrived and
it's your job to unpack them and put them in the store's display counter.

The truck (a list) is filled with boxes (tuples) of goods (strings). Among the
goods, there are various types of sausages. Straight sausages I, curvy
sausages), even twirly sausages @ and many more. The safest way to tell any
type of sausage apart from other goods is by the packaging [], used exclusively
by sausages. Make sure to ignore other goods, those will be taken care of by
someone else. Once you have unpacked all the sausages, just lay them out in the
display counter (string) in the same order in which they came in boxes with one
space " " in-between every sausage. Oh, and watch out for spoiled or damaged
sausage packs, did I tell you about those? The sausages are alwaygit s packed
in fours and each pack contains only one sausage type, so whenever there is any
irregularity, the sausages are probably spoiled or damaged and the whole pack
should be thrown out!

Now we're getting to the best part - your reward! Instead of money, you'll be
paid in something far better - sausages! Every fifth undamaged processed pack
of sausages doesn't go to the counter, instead it's yours to keep. Don't go
spending it all at once!

If the truck arrives completely empty, only with empty boxes or only with goods
that are not sausages, the display counter will simply stay empty "". Unlike
truck and boxes that may be empty, every existing product is a non-empty
string.
"""

import re


def unpack_sausages(truck):
    packages = [' '.join(package[1:-1])
                for box in truck for package in
                box if re.match(r'^\[(.)\1{3}\]$', package)]
    del(packages[4::5])
    return ' '.join(packages)


sausages = [("(-)", "[IIII]", "[))))]"), ("IuI", "[llll]"),
            ("[@@@@]", "UwU", "[IlII]"), ("IuI", "[))))]", "x"), ()]

print(unpack_sausages(sausages))
