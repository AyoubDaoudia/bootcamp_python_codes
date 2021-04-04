import datetime
from recipe import Recipe

class Book:
    def __init__(self,name,last_update,creation_date,recipe_list):
        self.name=name
        if type(name)!=str or name=="" :
            raise ValueError
        self.last_update=last_update
        self.creation_date=creation_date
        if type(recipe_list)!=dict or (len(recipe_list)!=3 or ("starter" not in recipe_list) or ("lunch" not in recipe_list) or ("dessert" not in recipe_list)) :
            raise ValueError
        self.recipe_list=recipe_list
        
    def get_recipe_by_name(self,name):
        L=[]
        starter=list(self.recipe_list["starter"])
        lunch=list(self.recipe_list["lunch"])
        dessert=list(self.recipe_list["dessert"])
        if matching(starter,lunch) or matching(lunch,dessert) or matching(dessert,starter):
            return "There are matching names in your recipe type list"
        if name in starter :
            return self.recipe_list["starter"][name]
        elif name in lunch :
            return self.recipe_list["lunch"][name]
        elif name in dessert :
            return self.recipe_list["dessert"][name]
        else:
            return "There is no recipe of that name."
        
    def get_recipe_by_types(self,recipe_type):
        if recipe_type=="starter" :
             return list(self.recipe_list["starter"])
        elif recipe_type=="lunch" :
             return list(self.recipe_list["lunch"])
        elif recipe_type=="dessert" :
             return list(self.recipe_list["dessert"])
        else:
            return "There is no recipe with that type."
        
    def add_recipe(self,recipe):
        if isinstance(recipe, Recipe)==False:
            print("Please create the recipe first then add it to the book.")
            return 
        self.recipe_list[recipe.recipe_type][recipe.name]=recipe
        self.last_update=datetime.datetime.now()
        return
    
    
def matching(d1,d2):
    for i in d1:
        if i in d2:
            return True
    
    
    
    
    
    
    