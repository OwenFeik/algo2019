import cv2
from utils import show_image, load_base

def mandelbrot(c, d):
    z = 0
    for i in range(d):
        z = (z ** 2) + c
        if abs(z) > 3:
            return i

    return -1

def draw_mandelbrot(i, d, _x = 0, _y = 0, _w = 2, _h = 2):

    width, height, _ = i.shape
    
    x_scale = width / (2 * _w)
    y_scale = height / (2 * _h)

    for x in range(-1 * (width // 2), width // 2):
        for y in range(-1 * (height // 2), height // 2):
            n = mandelbrot(complex((x / x_scale) + _x, (y / y_scale) + _y), d)
            
            r = int(255 * (n / d))
            g = int(255 * (n / d))
            b = int(255 * (n / d))

            cv2.circle(i, (x + (width // 2), y + 499), 1, (b, g, r))



i = load_base()
d = 20

draw_mandelbrot(i, d, -1, 0, .5, .5)

show_image(i)
