import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("../roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                res = round((r + 6*g + 3*b)/10)
                draw.point((x, y), (res + 40, res + 20, res))
image.show()
del draw
