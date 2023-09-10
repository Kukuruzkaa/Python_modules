from book import Book
from recipe import Recipe
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

if __name__ == "__main__":
 
# Let's create some Recipe first

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
    description="A good option for a light lunch",
    recipe_type="lunch"   
    )

    tourte_recipe = Recipe(
    name="Tourte",
    cooking_lvl=4,
    cooking_time=60,
    ingredients=["pastry dough", "meat", "vegetables", "spices"],
    description="A classic savory pie with a flaky pastry crust.",
    recipe_type="starter"
    )
    to_print = str(tourte_recipe)
    print(to_print)

    #Invalid recipes
    # cake = Recipe("Chocolate Cake", 7, 45, ["flour", "sugar", "cocoa powder", "eggs", "butter"], "", "dessert")
    salad = Recipe("Cezar", 3, -20, ["tomatoes", "onion", "chicken", "green salad", "salt"],"", "lunch")
    # soup = Recipe(1, 2, 30, ["tomatoes", "onion", "garlic", "vegetable broth", "salt"], "", "starter")
    # tourte = Recipe("Tourte", 4, 60, [], "", "starter")
    # tourte2 = Recipe("Tourte", 4, 60, ["pastry dough", "meat", "vegetables", "spices"], "", "")
    
    # Create a Cookbook and add the recipes
    print(f"{Fore.RED}Creating my Cookbook")
    my_cookbook = Book("My first Cookbook")
    print(my_cookbook)
    print(f"{Fore.GREEN}Adding the recipes to my Cookbook")

    try:
        my_cookbook.add_recipe(salad)
    except ValueError as e:
        print(e)

    my_cookbook.add_recipe(cake_recipe)
    my_cookbook.add_recipe(soup_recipe)
    my_cookbook.add_recipe(salad_recipe)
    my_cookbook.add_recipe(tourte_recipe)
    print(my_cookbook)

    #Test getting a recipe by name
    print(f"{Fore.YELLOW}Getting a recipe by name")
    recipe = my_cookbook.get_recipe_by_name("Chocolate Cake")
    if recipe:
        print(f"Found Recipe: {recipe.name}\n")
    else:
        print("Recipe not found.")

    # Test getting a recipe by type
    print(f"{Fore.BLUE}Getting a recipe by its type")
    types = my_cookbook.get_recipes_by_types("starter")
    for type in types:
        print(type)


