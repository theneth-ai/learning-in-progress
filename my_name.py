import sys

try:
    print("My name is",sys.argv[0])
except IndexError:
    print("Please provide your name in the terminal")
    print("Ex: python [file name].py [Your name]")
