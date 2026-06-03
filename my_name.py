import sys
try:
    print("Hello,my name is",sys.argv[1])
except IndexError:
    print("Please provide your first name in the terminal!")
    print("Ex: python [file name].py [Your name]")