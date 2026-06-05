import csv

people=[]
with open("pet_Name.csv") as info:
    line=csv.DictReader(info)
    for data in line:
        people.append({"name":data["Name"], "nickname": data["Nickname"]})


for person in sorted(people,key=lambda x:x["name"]):
    print(f"{person['name']} belongs to {person['nickname']}")