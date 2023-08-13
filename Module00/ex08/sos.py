import sys
import string

morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter.isalnum():
            cipher += morse[letter] + ' '
        elif letter.isspace():
            cipher += '/'
        else:
            print('ERROR')
            sys.exit(0)
    return cipher


def main():
    if (len(sys.argv) > 1):
        message = sys.argv
        del message[0]
        to_morse = ' '.join(message)
        res = encrypt(to_morse.upper())
        print (res)

if __name__ == "__main__":
    main()
