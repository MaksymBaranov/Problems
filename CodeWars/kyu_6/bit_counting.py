"""
https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
"""


def bit_counting(num):
    return str(bin(num)).count('1')


print(bit_counting(0))
print(bit_counting(4))
print(bit_counting(7))
print(bit_counting(9))
print(bit_counting(10))
print(bit_counting(1234))
print(bit_counting(11))
