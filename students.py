list=[]
with open("names.csv") as file:
    for line in file:
        row=line.rstrip().split(",")
        list.append(row)
        print(f"{row[0]} is in {row[1]}")

print(list[-1])