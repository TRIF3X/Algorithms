#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # compare the keys in ingredients to the keys in recipe
  # if a key is missing print 0
  # if all keys are present check how many times the ingredients can be divided into the recipe
  pass
       



print(recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 10, 'cookies': 100 },
  { 'milk': 198, 'butter': 52, 'flour': 10 }
))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))