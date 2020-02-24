import random
from PIL import Image, ImageDraw

image = Image.open("../bear.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
for x in range(width)[:-1]:
        for y in range(height):
                r = pix[x, y][0]
                r_right = pix[x + 1, y][0]
                g = pix[x, y][1]
                g_right = pix[x + 1, y][1]
                b = pix[x, y][2]
                b_right = pix[x + 1, y][2]
                draw.point((x, y), (128 + 2*(r - r_right), 128 + 2*(g - g_right), 128 + 2*(b - b_right)))
image.save("bearRelief.jpg")
del draw
