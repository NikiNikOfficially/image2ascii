from PIL import Image, ImageDraw, ImageFont
import math
import getopt
import sys

#Default Values
scaleFactor = 0.8
out_imgf = "output.jpg"
out_textf = "output.txt"
textimg = 0


arguments = sys.argv[1:]
args_s = "o:s:t"
args_l = ["output=", "scaleFactor=", "text"]

try:
    args, vals = getopt.getopt(arguments, args_s, args_l)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for arg, val in args:
    if arg in ("-o", "--output"):
        out_imgf = val
        out_textf = val
    elif arg in ("-s", "--scaleFactor"):
        scaleFactor = float(val)
    elif arg in ("-t", "--text"):
        textimg = 1

if not vals:
    print("Please provide an Image!")
    exit(1)

input_file = vals[0]


chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

oneCharWidth = 6
oneCharHeight = 8

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]



fnt = ImageFont.truetype('font/Lucon.ttf', 10)

im = Image.open(input_file)
width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()


if textimg:
    text_file = open(out_textf, "w")
else:
    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        if textimg:
            text_file.write(getChar(h))
        else:
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
    if textimg: text_file.write('\n')

if not textimg: outputImage.save(out_imgf)