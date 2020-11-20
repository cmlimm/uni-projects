import random
from PIL import Image, ImageDraw

image = Image.open("../bear.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
for x in range(width):
    for y in range(height):
        if y > height - height / width * x:
            draw.point((x,y),(255,0,255))

image.save("bearTest.jpg")
del draw
