# ==========================================
# 1. Terminal එකෙන් වචන ගන්න විදිහ (sys.argv)
# ==========================================
import sys

# Terminal එකෙන් වචනයක් දුන්නද බලනවා (නැත්නම් නවත්තනවා)
if len(sys.argv) != 2:
    sys.exit("Error: Please provide a word!")
    
# දුන්න වචනේ එළියට ගන්නවා (Index 1)
user_word = sys.argv[1] 
print("You typed:", user_word)


# ==========================================
# 2. අන්තර්ජාලයෙන් ඩේටා ගන්න විදිහ (Requests & JSON)
# ==========================================
import requests

# API ලින්ක් එකට request එකක් යවනවා (වේටර්ට ඕඩර් එක දෙනවා)
response = requests.get("API_LINK_HERE")

# ආපු ඩේටා ටික Python වලට තේරෙන Dictionary එකක් කරනවා
data = response.json()

# Dictionary එකෙන් ඕන ලාච්චුව (Key) ඇරලා ඩේටා ගන්නවා
print("My Data:", data["key_name"])