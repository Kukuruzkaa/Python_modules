
class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        error = self.check_values()
        if error:
            print(error)
            exit(1)

    def check_values(self):
        if not self.name:
            return "ERROR: empty name"
        elif not isinstance(self.name, str):
            return "ERROR: name is not a string"
        elif not isinstance(self.cooking_lvl, int):
            return "ERROR: cooking_lvl is not a number"
        elif not (1 <= self.cooking_lvl <= 5):
            return "ERROR: cooking_lvl is out of range"
        elif not isinstance(self.cooking_time, int):
            return "ERROR: cooking_time is not a number"
        elif self.cooking_time < 0:
            return "ERROR: cooking_time cannot be a negative number"
        elif len(self.ingredients) == 0:
            return "ERROR: ingredients list cannot be empty"
        elif not isinstance(self.description, str):
            return "ERROR: description is not a string"
        elif self.recipe_type not in ['starter', 'lunch', 'dessert']:
            return "ERROR: not existing recipe_type"
            
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Recipe: {self.name}\n" \
              f"Cooking level: {self.cooking_lvl}\n" \
              f"Cooking time: {self.cooking_time}\n" \
              f"Ingredients: {' ,'.join(self.ingredients)}\n" \
              f"Description: {self.description}\n" \
              f"Recipe type: {self.recipe_type}\n"
        return txt


