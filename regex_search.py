import re

text = "You can reach me at 076-1234567 today."

pattern = r"\d{3}-\d{7}"

match = re.search(pattern, text)
if match:
    print(f"Phone number found: {match.group()}")
else:
    print("Did not find a phone number.")
