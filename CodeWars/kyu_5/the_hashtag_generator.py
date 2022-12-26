"""
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
"""


def generate_hashtag(string):
    camel_case = "".join([word.capitalize() for word in string.split()])
    if 0 < len(camel_case) <= 140:
        return f'#{camel_case}'
    else:
        return False


print(generate_hashtag('      codewars        coDewars      '))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
