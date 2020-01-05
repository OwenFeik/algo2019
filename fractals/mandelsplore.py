# Owen Feik, 12K
# Program uses pygame
# Run "python -m pip install pygame" or "pip install pygame" before use
# Then run mandelsplore.py <depth> eg "python mandelsplore.py 100" to run mandelbrot up to 100 times


import pygame
import time # Update loading bar at intervals
import sys # Input depth

def loading_bar(p, b = 10):
    width, height = s.get_size()
    
    x = int(0.2 * width)
    y = int(0.7 * height)
    w = int(0.6 * width)
    h = int(0.05 * height)

    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(s, (255, 255, 255), rect)

    rect = pygame.Rect(x + b, y + b, (w - b) * p, h - (2 * b))
    pygame.draw.rect(s, (0, 0, 0), rect)
    pygame.display.update()

def mandelbrot(c, d):
    z = 0
    for i in range(d):
        z = (z ** 2) + c
        if abs(z) > 3:
            return i

    return -1

def draw_mandelbrot(size, d, _x = 0, _y = 0, _w = 2, _h = 2):

    width, height = size
    s = pygame.Surface(size)
    
    x_scale = width / (2 * _w)
    y_scale = height / (2 * _h)

    prevtime = time.time_ns()
    for x in range(-1 * (width // 2), width // 2):
        for y in range(-1 * (height // 2), height // 2):
            n = mandelbrot(complex((x / x_scale) + _x, (y / y_scale) + _y), d)
            
            r = max(int(255 * (n / d)), 0)
            g = max(int(255 * (n / d)), 0)
            b = max(int(255 * (n / d)), 0)

            colour = (r, g, b)

            p = x + (width // 2), y + (width // 2)

            s.set_at(p, colour)

            t = time.time_ns()
            if (t - prevtime) > 10000000:
                loading_bar((x + (width // 2)) / width)
                prevtime = t
    return s


pygame.init()
pygame.display.set_caption('Mandelbrot Explorer')
width, height = 1000, 1000
s = pygame.display.set_mode((width, height))

d = int(sys.argv[1]) if sys.argv[1].isnumeric() else 100
x, y, w, h = 0, 0, 2, 2

frames = [draw_mandelbrot((width, height), d, x, y, w, h)]
i = 0
u = True

running = True

while True:
    if u:
        s.blit(frames[i], (0, 0))
        pygame.display.update()
        u = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mx, my = event.pos
                x += ((mx - (width // 2)) / (width / (2 * w)))
                y += ((my - (height // 2)) / (height / (2 * h)))
                w /= 10
                h /= 10
                frames.append(draw_mandelbrot((width, height), d, x, y, w, h))
                u = True
                i += 1
            elif event.button == 3:
                if i > 0:
                    frames = frames[:-1]
                    i -= 1
                    u = True

