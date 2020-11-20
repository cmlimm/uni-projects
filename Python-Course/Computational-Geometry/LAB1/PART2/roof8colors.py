import random
from PIL import Image, ImageDraw

def clip(x):
    if x > 128:
        return 255
    else:
        return 0

image = Image.open("../roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
for x in range(width)[:-1]:
        for y in range(height):
                r = clip(pix[x, y][0])
                g = clip(pix[x, y][1])
                b = clip(pix[x, y][2])
                draw.point((x, y), (r, g, b))
image.save("roof8colors.jpg")
del draw
