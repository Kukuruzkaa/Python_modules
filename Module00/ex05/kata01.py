kata = {'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',}

bool(kata)
False
not kata
True

def main():
    if not kata:
        print ("Empty dictionnary")
    else:
        for language, name in kata.items():
            print(f'{language} was created by {name}')

if __name__ == "__main__":
    main()
