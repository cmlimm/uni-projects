import random
from PIL import Image, ImageDraw
from math import sqrt

image = Image.open("../winter.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

start = height / 3
finish = height / 2

for x in range(width):
        for y in range(height):
            r = sqrt((x - width/2)**2 + (y - height/2)**2)
            if r > finish:
                draw.point((x, y), (255, 255, 255))
            elif r < start:
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (r, g, b))
            else:
                q = (r - start) / (finish - start)
                r = round(pix[x, y][0]*(1 - q) + 255*q)
                g = round(pix[x, y][1]*(1 - q) + 255*q)
                b = round(pix[x, y][2]*(1 - q) + 255*q)
                draw.point((x, y), (r, g, b))
image.save("vignetteCircle.jpg")
del draw
