import requests
import sys

if len(sys.argv) !=2:
    sys.exit("Error:Please provide exactly one word! (Example: python req.py apple)")

print("Connecting to the API... Please wait...")

response=requests.get("https://official-joke-api.appspot.com/random_joke")
user_Data=response.json()

print("\n---Here is your joke---")
print("Setup:", user_Data["setup"])
print("Punchline:", user_Data["punchline"])
print("Type:", user_Data["type"])
print(user_Data)


