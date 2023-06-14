import string
import sys

def text_analyzer(text=None):

    '''This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.'''
    space_sum = 0
    upper_sum = 0
    lower_sum = 0
    punctuation_sum = 0
    if text is None:
        text = input("what is the text to analyze?\n ")
    if type(text) is str:
        for char in text:
            if char.isupper():
                upper_sum += 1
            elif char.islower():
                lower_sum += 1
            elif char in string.punctuation:
                punctuation_sum += 1
        space_sum = text.count(' ')
        text = set(text)
        print("The text contains {} character(s):".format(str(len(text) - space_sum)))
        print("- {} upper letter(s)".format(str(upper_sum)))
        print("- {} lower letter(s)".format(str(lower_sum)))
        print("- {} punctuation mark(s)".format(str(punctuation_sum)))
        print("- {} space(s)".format(str(space_sum)))
    else:
        print ("AssertionError: argument is not a string")

def main():
    if (len(sys.argv) < 2):
        text_analyzer()
    elif (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else:
        print("AssertionError: more than one argument are provided")

if __name__ == "__main__":
    main()

