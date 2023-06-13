import sys
import string

def text_analyzer(text=None):
    if text is None:
        print("What is the text to analyze?")
        text = input()
    if not isinstance(text, str):
        print("Error: not a string")

# $> python3
# >>> from count import text_analyzer
# >>> text_analyzer("Python 2.0, released 2000, introduced
# features like List comprehensions and a garbage collection
# system capable of collecting reference cycles.")
# The text contains 143 character(s):
# - 2 upper letter(s)
# - 113 lower letter(s)
# - 4 punctuation mark(s)
# - 18 space(s)

# >>> text_analyzer("Python is an interpreted, high-level,
# general-purpose programming language. Created by Guido van
# Rossum and first released in 1991, Python's design philosophy
# emphasizes code readability with its notable use of significant
# whitespace.")
# The text contains 234 character(s):
# - 5 upper letter(s)
# - 187 lower letter(s)
# - 8 punctuation mark(s)
# - 30 space(s)

# >>> text_analyzer()
# What is the text to analyze?
# >> Hello World!
# The text contains 8 character(s):
# - 2 upper letter(s)
# - 8 lower letter(s)
# - 1 punctuation mark(s)
# - 1 space(s)

# >>> text_analyzer(42)
# AssertionError: argument is not a string

# >>> print(text_analyzer.__doc__)
# This function counts the number of upper characters, lower characters,
# punctuation and spaces in a given text.