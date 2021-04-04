class Recipe:
    def __init__(self,name,cooking_lvl,cooking_time,ingredients,description,recipe_type):
        if name=='' or type(name)!=str:
            raise ValueError
        self.name=name
        if type(cooking_lvl)!=int or not(1<=cooking_lvl<=5):
            raise ValueError
        self.cooking_lvl=cooking_lvl
        if type(cooking_time)!=int or cooking_time<0:
            raise ValueError
        self.cooking_time=cooking_time
        if type(ingredients)!=list:
            raise ValueError
        self.ingredients=ingredients
        if type(description)!=str:
            raise ValueError
        self.description=description
        if recipe_type!="starter" and recipe_type!="lunch" and recipe_type!="dessert" :
            raise ValueError
        self.recipe_type=recipe_type
    def __str__(self):
        text="The {n} recipe is of level {l}, needs {t} min, uses the following ingredients {i},{d}it is taken as {r}".format(n=self.name,l=self.cooking_lvl,t=self.cooking_time,i=self.ingredients,d=self.description,r=self.recipe_type)
        return text
        