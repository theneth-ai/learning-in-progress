people=[]
with open("pet_Name.csv") as data:
    next(data) #Igonres the first line in the csv file
    for line in data:
        name,nickname=line.rstrip().split(',')
        getname={"name":name, "nickname":nickname}
        people.append(getname)

      
for getname in sorted(people,key=lambda get_name:get_name["name"]):
    print(f"{getname['name']} belongs to {getname['nickname']}")
