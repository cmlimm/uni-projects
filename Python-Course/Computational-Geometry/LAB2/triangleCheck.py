
import random
from PIL import Image, ImageDraw

image = Image.open("bear.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

# получаем y координату по координате x на прямой, заданной двумя точками
def get_y(p1, p2, x):
    y = p1[1] + (x - p1[0])*(p2[1] - p1[1])/(p2[0] - p1[0])
    return round(y)

def triangle (p1, p2, p3, color):
    p1, p2, p3 = sorted([p1, p2, p3])
    # если треугольник повернут вниз
    if p2[1] > get_y(p1, p3, p2[0]):
        for x in range(p1[0], p2[0]):
            for y in range(get_y(p1, p3, x), get_y(p1, p2, x)):
                draw.point((x, y), color)
        for x in range(p2[0], p3[0]):
            for y in range(get_y(p1, p3, x), get_y(p2, p3, x)):
                draw.point((x, y), color)
    # если треугольник повернут вверх
    else:
        for x in range(p1[0], p2[0]):
            for y in range(get_y(p1, p2, x), get_y(p1, p3, x)):
                draw.point((x, y), color)
        for x in range(p2[0], p3[0]):
            for y in range(get_y(p2, p3, x), get_y(p1, p3, x)):
                draw.point((x, y), color)

# В следующих строках задаются цвета треугольников и точки, по которым они строятся
black = (0,0,0)
green = (0,200,0)
red = (200,0,0)
blue = (0,0,200)
t1 = (0,height//4)
t2 = (width//2, 0)
t3 = (width//4, height//2)
t4 = (width-1,height//2)
t5 = (width//2,height//4)
t6 = (width*3//4,0)
t7 = (0,height//2)
t8 = (width//4,height-1)
t9 = (width//2,height*3//4)
t10 = (width-1,height*3//4)
t11 = (width*3//4,height//2)
t12 = (width//2,height-1)
# Ниже вызываем заливку 4-х треугольников для проверки работы программы
triangle(t1, t2, t3, green)
triangle(t4, t5, t6, red)
triangle(t7, t8, t9, blue)
triangle(t10, t11, t12, black)

image.show()
image.save("result.jpg")
del draw
