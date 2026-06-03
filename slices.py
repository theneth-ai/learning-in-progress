import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments") #Ends the program after displaying this message!

for arg in sys.argv[1:]: # Slices the list from index 1 to the end of the list
    print("Hello, my name is", arg) 