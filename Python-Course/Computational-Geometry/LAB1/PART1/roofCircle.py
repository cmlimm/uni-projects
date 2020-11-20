import random
from math import sqrt
from PIL import Image, ImageDraw

image = Image.open("../roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
centre = (round(width/2), round(height/2))
radius = height/4

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                if sqrt((centre[0] - x)**2+(centre[1] - y)**2) <= radius:
                    draw.point((x, y), (255, 128, 0))
                elif (x // 36 % 2 == 0) and (y < height - height/4) and (y > height/4):
                    draw.point((x, y), (0, 200, 0))
                else:
                    draw.point((x, y), (r, g, b))
image.save("roofCircle.jpg")
del draw
