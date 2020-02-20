import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("../roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
for x in range(width)[:-1]:
        for y in range(height):
                r = pix[x, y][0]
                r_right = pix[x + 1, y][0]
                g = pix[x, y][1]
                g_right = pix[x + 1, y][1]
                b = pix[x, y][2]
                b_right = pix[x + 1, y][2]
                draw.point((x, y), (128 + 2*(r - r_right), 128 + 2*(g - g_right), 128 + 2*(b - b_right)))
image.show()
del draw
