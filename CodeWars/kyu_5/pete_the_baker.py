"""
https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
"""


def cakes(recipe, available):
    if set(recipe).issubset(set(available)):
        return min([available[ingredients] // num for ingredients, num in recipe.items()])
    else:
        return 0


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))
