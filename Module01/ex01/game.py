import colorama
from colorama import Fore

class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
    

class Stark(GotCharacter):
    '''A class representing the Stark family. Or when bad things happen to good people.'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    '''A class representing the Lannister family. Or when the love of your life is your sister.'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"
    
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False

class Targaryen(GotCharacter):
    '''A class representing the Targaryen family. Or when your children are dragons.'''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire And Blood"
    
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False


if __name__ == "__main__":

    print(f"{Fore.GREEN}Creating the powerfull families\n")

    jaime = Lannister('Jaime')
    print(f"{Fore.RED}Object stucture: {jaime.__dict__}")
    print(f"{Fore.YELLOW}Family description: {jaime.__doc__}")
    print(f"{Fore.BLUE}House words: ", end="")
    jaime.print_house_words()
    print(f"{Fore.GREEN}Is alive? - ", jaime.is_alive)
    jaime.die()
    print(f"{Fore.MAGENTA}Is alive? - ", jaime.is_alive)
    print()

    daenerys = Targaryen('Daenerys')
    print(f"{Fore.RED}Object stucture: {daenerys.__dict__}")
    print(f"{Fore.YELLOW}Family description: {daenerys.__doc__}")
    print(f"{Fore.BLUE}House words: ", end="")
    daenerys.print_house_words()
    print(f"{Fore.GREEN}Is alive? - ", daenerys.is_alive)
    daenerys.die()
    print(f"{Fore.MAGENTA}Is alive? - ", daenerys.is_alive)