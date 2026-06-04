people=[]
with open("pet_Name.csv") as data:
    next(data) #Igonres the first line in the csv file
    for line in data:
        name,nickname=line.rstrip().split(',')
        people.append(f"{name} called {nickname}")

print(people,'\n')        
for name in sorted(people):
    print(name)
