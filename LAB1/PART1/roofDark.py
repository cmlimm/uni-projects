import random
from PIL import Image, ImageDraw

image = Image.open("../roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
for x in range(width):
        for y in range(height):
                r = round(pix[x, y][0]/2)
                g = round(pix[x, y][1]/2)
                b = round(pix[x, y][2]/2)
                draw.point((x, y), (r, g, b))
image.save("roofDark.jpg")
del draw
