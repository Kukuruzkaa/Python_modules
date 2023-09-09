from book import Book
from recipe import Recipe

if __name__ == "__main__":
 
# Create some Recipe objects
    cake_recipe = Recipe(
    name="Chocolate Cake",
    cooking_lvl=3,
    cooking_time=45,
    ingredients=["flour", "sugar", "cocoa powder", "eggs", "butter"],
    description="A delicious chocolate cake for any occasion.",
    recipe_type="dessert"
    )

    soup_recipe = Recipe(
    name="Tomato Soup",
    cooking_lvl=2,
    cooking_time=30,
    ingredients=["tomatoes", "onion", "garlic", "vegetable broth", "salt"],
    description="A comforting tomato soup recipe.",
    recipe_type="starter"   
    )

    salad_recipe = Recipe(
    name="Cezar",
    cooking_lvl=3,
    cooking_time=20,
    ingredients=["tomatoes", "onion", "chicken", "green salad", "salt"],
    description="A comforting tomato soup recipe.",
    recipe_type="lunch"   
    )
    
    # Create a Cookbook and add the recipes
    my_cookbook = Book("My Cookbook")
    my_cookbook.add_recipe(cake_recipe)
    my_cookbook.add_recipe(soup_recipe)
    my_cookbook.add_recipe(salad_recipe)

    # Test getting a recipe by name
    # found_recipe = my_cookbook.get_recipe_by_name("Chocolate Cake")
    # if found_recipe:
    #     print(f"Found Recipe: {found_recipe.name}")
    # else:
    #     print("Recipe not found.")

    # Print Cookbook information
    print(my_cookbook)