info=[]
with open("names_DB.txt") as my_file: #Open with default mode-'r'
    for line in my_file:
        info.append(line.rstrip())
for data in sorted(info): #Accessing and sorting the data in the name_DB file
    print("How are you", data.title())