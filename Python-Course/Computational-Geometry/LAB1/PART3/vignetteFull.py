import random
from PIL import Image, ImageDraw
from math import sqrt

image = Image.open("../park.jpg")
draw = ImageDraw.Draw(image)
w  = image.size[0]
h = image.size[1]
pix = image.load()

q2Start = (h / 2)**2 / (h / 3)**2
q2Finish = 1

for x in range(w):
        for y in range(h):
            q1 = (x - w / 2)**2 / (w / 2)**2 + (y - h / 2)**2 / (h / 2)**2
            q2 = (x - w / 2)**2 / (w / 3)**2 + (y - h / 2)**2 / (h / 3)**2
            if q1 > 1:
                draw.point((x, y), (255, 255, 255))
            elif q2 < 1:
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (r, g, b))
            else:
                q = (q2 - q2Finish)/(q2Start - q2Finish)
                r = round(pix[x, y][0]*(1 - q) + 255*(q))
                g = round(pix[x, y][1]*(1 - q) + 255*(q))
                b = round(pix[x, y][2]*(1 - q) + 255*(q))
                draw.point((x, y), (r, g, b))
image.save("vignetteFull.jpg")
del draw
