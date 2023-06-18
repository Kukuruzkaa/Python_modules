import string
import sys

def filter(line, n):
    list = line.split()
    new_list = []
    for word in list:
        letters = sum(1 for char in word if char not in string.punctuation)
        if letters > int(n):
            new_list.append(word)
    return new_list   
    
def main():
    if (len(sys.argv) != 3):
        print('ERROR')
    else:
        try:
            list = filter(sys.argv[1], sys.argv[2])
            print(list)
        except ValueError:
            print('ERROR')
            
if __name__ == "__main__":
    main()