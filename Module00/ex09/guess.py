import random

def main():
    number = random.randint(1,99)
    print('''This is an interactive guessing game!
    You have to enter a number between 1 and 99 to find out the secret number.
    Type 'exit' to end the game.
    Good luck!\n''')

    attempt = 0
    while True:
        attempt += 1
        guess = (input('What\'s your guess between 1 and 99?\n'))
        if guess == 'exit':
            print('Goodbye!')
            exit(0)
        try:
            guess_nb = int(guess)
            if (guess_nb > number):
                print('Too high!')
            elif (guess_nb < number):
                print('Too low!')
            else:
                if (guess_nb == 42):
                    print('The answer to the ultimate question of life, the universe and everything is 42')
                elif (attempt == 1):
                     print('Congratulations! You got it on your first try!')
                else:
                    print(f'Congratulations, you\'ve got it!\nYou won in {attempt} attempts!')
                break
        except ValueError:
            print('That\'s not a number.')

if __name__ == "__main__":
    main()
