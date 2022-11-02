"""
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
"""


def array_diff(lst1, lst2):
    return [elm for elm in lst1 if elm not in lst2]


print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2], [1]))
print(array_diff([1, 2, 2], [2]))
print(array_diff([1, 2, 2], []))
print(array_diff([], [1, 2]))
print(array_diff([1, 2, 3], [1, 2]))
