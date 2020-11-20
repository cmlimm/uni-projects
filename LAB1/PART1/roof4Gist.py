import random
from PIL import Image, ImageDraw

image = Image.open("../roof.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

gistRed = [0]*256
gistGreen = [0]*256
gistBlue = [0]*256
gistBrightness = [0]*256

for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            gistRed[r] += 1
            gistGreen[g] += 1
            gistBlue[b] += 1
            gistBrightness[round((r+g+b)/3)] += 1

maximumRed = max(gistRed)
maximumGreen = max(gistGreen)
maximumBlue = max(gistBlue)
maximumBrightness = max(gistBrightness)

gistRed = [round((elem*height)/(2*maximumRed)) for elem in gistRed]
gistGreen = [round((elem*height)/(2*maximumGreen)) for elem in gistGreen]
gistBlue = [round((elem*height)/(2*maximumBlue)) for elem in gistBlue]
gistBrightness = [round((elem*height)/(2*maximumBrightness)) for elem in gistBrightness]

for x in range(0, 255):
        for y in range(gistGreen[x]):
                draw.point((2*x, round(height/2) - y), (0, 255, 0))
                draw.point((2*x + 1, round(height/2) - y), (0, 255, 0))

for x in range(0, 255):
        for y in range(gistRed[x]):
                draw.point((round(width/2) + 2*x, round(height/2) - y), (255, 0, 0))
                draw.point((round(width/2) + 2*x + 1, round(height/2) - y), (255, 0, 0))

for x in range(0, 255):
        for y in range(gistBrightness[x]):
                draw.point((2*x, height - y), (200, 200, 200))
                draw.point((2*x + 1, height - y), (200, 200, 200))

for x in range(0, 255):
        for y in range(gistBlue[x]):
                draw.point((round(width/2) + 2*x, height - y), (0, 0, 255))
                draw.point((round(width/2) + 2*x + 1, height - y), (0, 0, 255))
image.save("roof4Gist.jpg")
del draw
