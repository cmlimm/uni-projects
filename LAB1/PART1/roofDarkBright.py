import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("../roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
        for y in range(height):
                r = round(pix[x, y][0] + (x - width/2)/4)
                g = round(pix[x, y][1] + (x - width/2)/4)
                b = round(pix[x, y][2] + (x - width/2)/4)
                draw.point((x, y), (r, g, b))

image.show()
del draw
