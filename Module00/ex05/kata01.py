kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main():
   for language, name in kata.items():
       print(f'{language} was created by {name}')

if __name__ == "__main__":
    main()
