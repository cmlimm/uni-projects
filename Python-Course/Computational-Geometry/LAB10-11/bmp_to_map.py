import random
from PIL import Image, ImageDraw

def height_map(filename, scale):
    image = Image.open(filename)
    width  = image.size[0]
    height = image.size[1]
    pix = image.load()
    array = [[0]*width for _ in range(height)]
    for x in range(width)[:-1]:
            for y in range(height):
                    array[x][y] = round(pix[x, y]*scale, 3)
    return array

if __name__ == '__main__':
    img_path = 'map.bmp'
    print(height_map(img_path, 0.05))
