import random
from PIL import Image, ImageDraw

park = Image.open("../park.jpg")
winter = Image.open("../winter.jpg")
draw = ImageDraw.Draw(park)
width  = park.size[0]
height = park.size[1]
pixPark = park.load()
pixWinter = winter.load()

start = width // 3
finish = start * 2

for x in range(width):
        for y in range(height):
            if x < start:
                r = pixPark[x, y][0]
                g = pixPark[x, y][1]
                b = pixPark[x, y][2]
                draw.point((x, y), (r, g, b))
            elif x > finish:
                r = pixWinter[x, y][0]
                g = pixWinter[x, y][1]
                b = pixWinter[x, y][2]
                draw.point((x, y), (r, g, b))
            else:
                q = (x - start) / (finish - start)
                r = round(pixPark[x, y][0]*(1 - q) + pixWinter[x, y][0]*q)
                g = round(pixPark[x, y][1]*(1 - q) + pixWinter[x, y][1]*q)
                b = round(pixPark[x, y][2]*(1 - q) + pixWinter[x, y][2]*q)
                draw.point((x, y), (r, g, b))
park.save("opacity.jpg")
del draw
