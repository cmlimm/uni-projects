import random
from PIL import Image, ImageDraw

def auto_levels(x, a, b):
    if a < x < b:
        return round((x - a) * 255 / (b - a))
    else:
        return x

def findMin(gist, min):
    i = 0
    while gist[i] <= min:
        i += 1
    return i

def findMinReverse(gist, min):
    i = 255
    while gist[i] <= min:
        i -= 1
    return i

image = Image.open("../lego.jpg")
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

min = 200
ra = findMin(gistRed, min)
rb = findMinReverse(gistRed, min)

ga = findMin(gistGreen, min)
gb = findMinReverse(gistGreen, min)

ba = findMin(gistGreen, min)
bb = findMinReverse(gistGreen, min)

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (auto_levels(r, ra, rb), auto_levels(g, ga, gb), auto_levels(b, ba, bb)))

image.save("legoAutoLevels.jpg")
del draw
