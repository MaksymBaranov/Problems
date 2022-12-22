"""
https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
"""


def two_sum(numbers, target):
    for ind_1 in range(len(numbers)):
        for ind_2 in range(ind_1 + 1, len(numbers)):
            if numbers[ind_1] + numbers[ind_2] == target:
                return [ind_1, ind_2]


print(two_sum([1, 2, 3], 4))
print(two_sum([1234, 5678, 9012], 14690))
print(two_sum([2, 2, 3], 4))
