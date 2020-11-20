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
                if x >= y*(width/height):
                    draw.point((x, y), (255, 255, 0))
                else:
                    draw.point((x, y), (r, g, b))
image.save("roofHalfYellow.jpg")
del draw
