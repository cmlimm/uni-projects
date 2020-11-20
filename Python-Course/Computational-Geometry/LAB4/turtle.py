import random
from math import cos, sin, pi
from PIL import Image, ImageDraw

def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0

def line(x1, y1, x2, y2, draw):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1)
            for x in range(x1, x2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dX:
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY

class Turtle:
    def __init__(self, x, y, angle, draw):
        self.x = x
        self.y = y
        self.angle = angle
        self.draw = draw

    def move(self, count):
        self.new_x = self.x + round(cos(self.angle)*count)
        self.new_y = self.y + round(sin(self.angle)*count)
        line(self.x, self.y, self.new_x, self.new_y, self.draw)
        self.x = self.new_x
        self.y = self.new_y

    def rotate(self, angle):
        self.angle += angle

image = Image.open("roof_half.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей

for x in range(width):
        for y in range(height):
                draw.point((x, y), (255, 255, 255))

turtle = Turtle(width//2, height//2, 0, draw)
turtle.move(100)
turtle.rotate(pi/6)
turtle.move(100)
turtle.rotate(-2*pi/6)
turtle.move(100)

image.show()
image.save("turtle.jpg")

del draw
