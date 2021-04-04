import time
from recipe import Recipe

class Book:
    def __init__(self,name,last_update,creation_date,recipes_list):
        self.name=name
        if type(name)!=str or name!="" :
            raise ValueError
        self.last_update=last.update
        self.creation_date=creation_date
        if type(recipe_list)!=list or (len(recipe_list)!=3 or ("starter" not in recipe_list) or ("lunch" not in recipe_list) or ("dessert" not in recipe_list)) :
            raise ValueError
        self.recipe_list=recipe_list
        
    def get_recipe_by_name(self,name):
        