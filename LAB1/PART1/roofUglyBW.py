import random
from PIL import Image, ImageDraw

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
                res = round((r + 6*g + 3*b)/10)
                if res > 110:
                    draw.point((x, y), (255, 255, 255))
                else:
                    draw.point((x, y), (0, 0, 0))
image.save("roofUglyBW.jpg")
del draw
