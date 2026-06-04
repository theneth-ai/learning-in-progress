file=open("names_DB.txt", "a")  #It tells open the .txt file using 'Append Mode"
count=1
while count<=5 :
    name=input("Type your name: ")
    file.write(f"{name}\n") 
    count+=1
file.close()
print("Names saved successfully!")
