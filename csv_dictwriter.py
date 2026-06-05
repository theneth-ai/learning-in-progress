import csv
name=input("Enter your name: ")
nickname=input("Enter your nickname: ")

with open("pet_Name.csv", "a") as information:
    writer=csv.DictWriter(information,fieldnames=["Name","Nickname"])
    writer.writerow({"Name": name,"Nickname":nickname})