

def count_bits(n):
    return str(bin(n))[2:].count('1')


print(count_bits(4))
