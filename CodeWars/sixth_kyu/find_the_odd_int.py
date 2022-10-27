'''
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
'''


def find_it(seq):
    numbers_count = {}
    for elm in seq:
        numbers_count[elm] = numbers_count.get(elm, 0) + 1
    for key, val in numbers_count.items():
        if val % 2 != 0:
            return key


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_it([10]))
print(find_it([10, 10, 10]))
print(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]))
print(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]))

# I want to work with branches
