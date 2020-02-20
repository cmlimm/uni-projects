import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

def auto_levels(x, a, b):
    if a < x < b:
        return round((x - a) * 255 / (b - a))
    else:
        return x

image = Image.open("../lego.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей

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

ra = gistRed.index(1)
rb = gistRed[::-1].index(1)

ga = gistGreen.index(1)
gb = gistGreen[::-1].index(1)

ba = gistBlue.index(1)
bb = gistBlue[::-1].index(1)

print(gistRed)
print(gistGreen)
print(gistBlue)

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (auto_levels(r, ra, rb), auto_levels(g, ga, gb), auto_levels(b, ba, bb)))

image.show()
del draw
