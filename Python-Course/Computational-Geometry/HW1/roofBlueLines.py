import random
from math import sqrt
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("../LAB1/roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
r = height // 14 #Получаем, что r = 77

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                if y // 77 % 2 == 1:
                    draw.point((x, y), (0, 0, 200))
                else:
                    draw.point((x, y), (r, g, b))
image.show()
del draw
