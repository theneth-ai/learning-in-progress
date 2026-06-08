import re

text = "I ordered 3 pizzas and 12 sodas for $45."

pattern = r"\d+" 

numbers = re.findall(pattern, text)
print(numbers) 
 #(Output): ['3', '12', '45']