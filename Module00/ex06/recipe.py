
cookbook = {
    'Sandwich': {
        'ingridients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingridients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingridients': ['avocado', 'tomatoes', 'spinch'],
        'meal': 'lunch',
        'prep_time': 15
    },
}           

def print_recipe_names(book):
        print('The recipes names are: {}'.format(', '.join('{}'.format(i) for i in book.keys())))

def print_recipe(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f'\nRecipe for {recipe_name}:')
        print(f'    Ingredients list: {recipe["ingridients"]}')
        print(f'    Type of meal: {recipe["meal"]}.')
        print(f'    It\'s preparation time is: {recipe["prep_time"]} minutes.\n')
    else:
        print(f'Recipe not found for: {recipe_name}')
        
def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        print(f'Recipe deleted: {recipe_name}')
        del(recipe_name)  
    else:
        print(f'Impossible to delete the recipe for: {recipe_name} - invalid recipe name')

def add_recipe():
    recipe_name = input("Enter a name:\n")
    pre_ingridients = input("Enter ingridients:\n")
    ingridients = []
    while pre_ingridients:
        ingridients.append(pre_ingridients)
        pre_ingridients = input()     
    meal = input("Enter a meal type:\n")
    prep_time = int(input("Enter a preparation time:\n"))
    
    recipe = {
        'ingridients': ingridients,
        'meal': meal,
        'prep_time': prep_time
    }
    cookbook[recipe_name] = recipe
    print()

def main():
    print('''Welcome to the Python Cookbook !\nList of availbale options:
    1: Add a receipe
    2: Delete a receipe
    3: Print a add_recipe
    4: Print the cookbook
    5: Quit\n''')
    option = 0
    while True:
        try:
            option = int(input('Please select an option:\n>> '))
            print()
        except ValueError:
            option = 0
        if option == 1:
            add_recipe()
        elif option == 2:
            recipe_name = input('Please enter the recipe name to delete:\n>> ')
            delete_recipe(recipe_name)
        elif option == 3:
            recipe_name = input('Please enter a recipe name to get its details:\n>> ')
            print_recipe(recipe_name)
        elif option == 4:
            print_recipe_names(cookbook)
        elif option == 5:
            print('Cookbook closed, Goodbye!')
            break
        else:
            print('''Sorry, this option does not exist.\nList of availbale options:
            1: Add a receipe
            2: Delete a receipe
            3: Print a add_recipe
            4: Print the cookbook
            5: Quit\n''')
        
if __name__ == "__main__":
    main()