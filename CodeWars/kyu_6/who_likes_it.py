"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""


def likes(name):
    # First solution
    if not name:
        return 'no one likes this'
    elif len(name) == 1:
        return f'{name[0]} likes this'
    elif len(name) == 2:
        return f'{name[0]} and {name[1]} like this'
    elif len(name) == 3:
        return f'{name[0]}, {name[1]} and {name[2]} like this'
    else:
        return f'{name[0]}, {name[1]} and {len(name[2:])} others like this'


def likes2(name):
    # Solution from answers. Should repeat the format function
    answers = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }
    length = len(name)
    return answers[min(4, length)].format(*name, others=length - 2)


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
print(likes2([]))
print(likes2(["Peter"]))
print(likes2(["Jacob", "Alex"]))
print(likes2(["Max", "John", "Mark"]))
print(likes2(["Alex", "Jacob", "Mark", "Max"]))