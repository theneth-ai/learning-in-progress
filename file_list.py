name_list=[]
count=0
for x in range(3):
    name=input("Type your name: ")
    name_list.append(name)
while count<len(name_list):
    print(f"This is {name_list[count]}")
    count=count+1

print("Execution Completed!")
    
