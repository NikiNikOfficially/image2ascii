from PIL import Image, ImageDraw, ImageFont
import math
import numpy as np

#chars = "abcdefghijklmnopqrstuvwxyzäöüABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ0123456789!§$&/()?{[]}\\#"
chars = input("Enter Characters>> ")
l = {}

fnt = ImageFont.truetype("font/Lucon.ttf", 100)

for char in chars:
    img = Image.new("RGB", (60, 80), color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((0, 0), char, font=fnt, fill=(255, 255, 255))
    im = img.convert("LA")
    image = np.array(im)
    
    avg = 0
    for y in image:
        for px in y:
            avg += px[0]
    avg = int(avg/4800)

    if avg in l:
        l[avg].append(char)
    else:
        l[avg] = [char]

ll = list(l.keys())
ll.sort()
out = []
for i in ll:
    out.append(l[i])

print(out)
