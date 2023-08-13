import string
import sys

def filter(line, n):
    cleaned_line ="".join(char for char in line if char not in string.punctuation)
    list = cleaned_line.split()
    new_list = []
    for word in list:
        if len(word) > int(n):
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