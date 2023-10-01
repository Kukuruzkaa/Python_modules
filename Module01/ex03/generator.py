import colorama
from colorama import Fore
import random

colorama.init(autoreset=True)

def my_random(list):
    lst_len = len(list)
    for i in range(0, lst_len):
        i = random.randint(0, lst_len - 1)
        yield list[i]

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings. 
        option precise if a action is performed to the substrings before it is yielded.'''
    if not isinstance(text, str) or sep!= " ":
        yield "Argument error"
    wordset = text.split(sep)
    if option == "shuffle":
        wordset = my_random(wordset)
    elif option == "unique":
        wordset = list(set(wordset))
    elif option == "ordered":
        wordset.sort()
    for word in wordset:
        yield word

if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    print(f"{Fore.YELLOW}Without option:")
    for word in generator(text, sep=" "):
        print(word)
    print()

    print(f"{Fore.YELLOW}Shuffle option:")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print()
    
    print(f"{Fore.YELLOW}Ordered option:")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print()

    print(f"{Fore.YELLOW}Unique option:")
    text2 = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text2, sep=" ", option="unique"):
        print(word)