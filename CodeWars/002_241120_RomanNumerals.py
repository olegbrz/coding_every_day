"""TODO: create a RomanNumerals helper object

| Symbol | Value |
|----------------|
| I      |  1    |
| V      |  5    |
| X      |  10   |
| L      |  50   |
| C      |  100  |
| D      |  500  |
| M      |  1000 |

"""
ld = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

dec = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
rom = ('M',  'CM', 'D', 'CD', 'C', 'XC',
       'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')


class RomanNumerals:

    @staticmethod
    def from_roman(roman):
        sum_ = 0
        for num in range(len(roman)):
            val = ld[roman[num]]
            if num + 1 < len(roman) and val < ld[roman[num+1]]:
                sum_ -= ld[roman[num]]
            else:
                sum_ += ld[roman[num]]
        return sum_

    @staticmethod
    def to_roman(decimal):
        roman = []
        for i in range(len(dec)):
            count = int(decimal / dec[i])
            roman.append(rom[i] * count)
            decimal -= dec[i] * count
        return ''.join(roman)


RomanNumerals.from_roman('IX')
