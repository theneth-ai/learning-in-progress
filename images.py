import sys
from PIL import Image

image_list = []

# අනිවාර්යයෙන්ම sys.argv[1:] වෙන්න ඕනේ (පයිතන් ෆයිල් එක අතෑරලා පින්තූර ටික විතරක් ගන්න)
for argument in sys.argv[1:]:
    image = Image.open(argument)
    image_list.append(image)

if len(image_list) >= 2:
    image_list[0].save(
        "costume.gif", 
        save_all=True, 
        append_images=image_list[1:], 
        duration=200, 
        loop=0
    )
    print("GIF created completed.")
else:
    print("Please give at least two images!")