import re

text = "My secret code is 847392 and my pin is 1234."

pattern = r"\d+"

censored_text = re.sub(pattern, "****", text)
print(censored_text)
