with open("names_DB.txt",'r') as my_file: 
    #wih- Auto closes the file
        #as my_file- This is the given name for the opened file inside the code'''                                      
      data=my_file.readlines() #Reading all of these lines with a new line
for line in data:
    print("My name is",line.rstrip())  #rstrip() removes the extra newline