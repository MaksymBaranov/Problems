"""
https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
"""


def stock_list(art_list, category_list):
    category_dict = {key: 0 for key in category_list}
    for string in art_list:
        category, number = string.split()
        for key in category_dict:
            if key == category[0]:
                category_dict[key] += int(number)

    return ' - '.join([f'({key} : {val})'for key, val in category_dict.items()]) if sum(category_dict.values()) > 0 else ''


print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"]))
