#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches_list = []
    for recipe_ingredient in recipe:
        try:
            possible_batches = (
                ingredients[recipe_ingredient]) // (recipe[recipe_ingredient])
        except:
            possible_batches = 0   # no batches,  missing ingredient
        batches_list.append(possible_batches)
    return sorted(batches_list)[0]


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
