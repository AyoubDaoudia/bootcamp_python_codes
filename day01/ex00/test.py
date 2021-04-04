from book import Book
from recipe import Recipe
import datetime


salad=Recipe("Salad",2,10,["tomatoes","onion","lettuce"]," this is a salad,","starter")
sandwich=Recipe("Sandwich",3,15,["ham","bread","cheese"],"this is a sandwich, ","lunch")
cake=Recipe("Cake",4,60,["flour","sugar","water"],"this is a cake, ","dessert")

List={
      "starter":{salad.name:salad},
      "lunch":{sandwich.name:sandwich},
      "dessert":{cake.name:cake}
      }

print(sandwich)
print()

Eat=Book("Eat",datetime.datetime.now(),datetime.datetime.now(),List)

print(Eat.get_recipe_by_types("lunch"))
print()

print(Eat.get_recipe_by_name("Sandwich"))
print()

Eat.add_recipe("Pizza")
print()

pizza=Recipe("Pizza",4,45,["flour","olives","bacon","pepper"],"it is a pizza, ","lunch")

Eat.add_recipe(pizza)

print(Eat.get_recipe_by_types("lunch"))
print()