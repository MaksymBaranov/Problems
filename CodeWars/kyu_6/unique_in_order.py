"""
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
"""


def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    else:
        final = [iterable[0]]
    for elm in iterable[1:]:
        if final[-1] != elm:
            final.append(elm)
    return final


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order(''))
print(unique_in_order('A'))
print(unique_in_order('AA'))
