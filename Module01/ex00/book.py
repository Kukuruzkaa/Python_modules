from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}
       
    
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list.keys():
            for recipe in self.recipes_list[recipe_type]:
                if recipe == name:
                    return recipe
        return None      
                   
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list.keys():
            return self.recipes_list[recipe_type]
        else:
            print("Invalid recipe type")
    
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) is Recipe:
            self.recipes_list[recipe.recipe_type].append(recipe)
            print(f"You added the recipe of {recipe.name}")
            self.last_update = datetime.now()
        else:
            print("Invalid recipe type")
    
    
    def __str__(self):
        return f"Cookbook: {self.name}\n" \
                f"Last Update: {self.last_update}\n" \
                f"Creation Date: {self.creation_date}\n" \
                f"Recipes: {len(self.recipes_list['starter'])} starters, " \
                f"{len(self.recipes_list['lunch'])} lunch recipes, " \
                f"{len(self.recipes_list['dessert'])} dessert recipes"

