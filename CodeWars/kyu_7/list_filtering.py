'''
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
'''


def filter_list(l):
    'return a new list with the strings filtered out'
    return [elm for elm in l if isinstance(elm, int)]


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
