"""
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
"""


def alphabet_position(text):
    return ' '.join([f'{ord(symbol) - 96}' for symbol in text.lower() if symbol.isalpha()])


print(alphabet_position('abc def ghj, klm obr s'))
print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
