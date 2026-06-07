email=input("Enter your e-mail here: ")

username,domain=email.split("@")
if username and domain.endswith(".com"):
    print("Valid")

else:
    print("Invalid")
