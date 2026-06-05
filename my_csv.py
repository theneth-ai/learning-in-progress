import csv
people=[]
with open("pet_Name.csv") as data:
    next(data) #Igonres the first line in the csv file
    reader=csv.reader(data) #instead of split and rsrtip
    for name,nickname in reader:
        people.append({"name":name, "nickname": nickname})


      
for person in sorted(people,key=lambda x:x["name"]):
    print(f"{person['name']} belongs to {person['nickname']}")
