import random
from PIL import Image, ImageDraw

image = Image.open("../roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
gistGreen = [0]*256
for x in range(width):
        for y in range(height):
            gistGreen[pix[x, y][1]] += 1
maximum = max(gistGreen)
gistGreen = [round((elem*height)/(2*maximum)) for elem in gistGreen]
for x in range(0, 255):
        for y in range(gistGreen[x]):
                draw.point((2*x, round(height/2) - y), (0, 255, 0))
                draw.point((2*x + 1, round(height/2) - y), (0, 255, 0))
image.save("roofGist.jpg")
del draw
