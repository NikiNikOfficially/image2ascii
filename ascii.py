from PIL import Image, ImageDraw, ImageFont
from random import choice
import math
import getopt
import sys

#Default Values
scaleFactor = 0.8
out_imgf = "output.jpg"
out_textf = "output.txt"
textimg = 0
bg = (0, 0, 0)

arguments = sys.argv[1:]
args_s = "o:s:tb:"
args_l = ["output=", "scaleFactor=", "text", "background="]

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
    elif arg in ("-b", "--background"):
        i = val.split(",")
        bg = (int(i[0]), int(i[1]), int(i[2]))

if not vals:
    print("Please provide an Image!")
    exit(1)

input_file = vals[0]

charArray = [['!'], ['/', '\\'], ['i'], ['r', '(', ')'], ['j', '[', ']', '}'], ['L', '{'], ['l', 'J'], ['y'], ['c', 'v'], ['T', 'Y', '?'], ['t', '7'], ['s'], ['C', 'F'], ['x', 'z', 'I'], ['1'], ['V'], ['3', '5'], ['f', '2'], ['n', 'u', 'S'], ['U', 'X', 'Z'], ['o', 'P'], ['a', 'e', 'A', 'E', 'K', '4'], ['§'], ['q'], ['g', 'p', 'ü'], ['k', 'G', 'Ü'], ['ö'], ['w', 'ä', 'H', 'Ä'], ['$'], ['h', 'O', 'Q'], ['N', 'R'], ['m', 'D', '6', '9'], ['0'], ['b', 'd'], ['#'], ['Ö'], ['B'], ['M', 'W'], ['8'], ['&']]

#chars = "$@B%8&WM#IoahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!l*;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
#charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

oneCharWidth = 15
oneCharHeight = 20

def getChar(inputInt):
    return choice(charArray[math.floor(inputInt*interval)])



fnt = ImageFont.truetype('font/Lucon.ttf', 25)

im = Image.open(input_file)
if input_file.split(".")[-1] == "png":
    im = im.convert("RGB")
width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()


if textimg:
    text_file = open(out_textf, "w")
else:
    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=bg)
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
