import random
from PIL import Image, ImageDraw

def clip(x):
    if x < 64:
        return 0
    if x < 128:
        return 85
    if x <= 192:
        return 170
    if x > 192:
        return 255

image = Image.open("../roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                res = clip(round((r + 6*g + 3*b)/10))
                draw.point((x, y), (res, res, res))
image.save("roof4colorsGray.jpg")
del draw
