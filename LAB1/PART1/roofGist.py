import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("../roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
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
image.show()
del draw
