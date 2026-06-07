import re
email=input("Enter your e-mail here: ").strip()
if re.search(".+@.+", email):
    print("Valid email")
else:
    print("Invalid email")

