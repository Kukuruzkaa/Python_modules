import sys

if len(sys.argv) > 1:
    newStr = ' '.join(sys.argv[1:])
    print(newStr[::-1].swapcase())