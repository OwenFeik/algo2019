import cv2
import math

colour = (255, 255, 255)

def draw_line(image, x1, y1, x2, y2):
    cv2.line(image, (int(x1), int(y1)), (int(x2), int(y2)), colour)

def show_image(image):
    while True:
        cv2.imshow('', image)

        key = cv2.waitKey(1000) & 255
        if key == ord('q'):
            cv2.destroyAllWindows()
            break

def koch_snowflake(image, depth, side, _x1, _y1, _x2, _y2):
    side = side / 3
    bearing = math.atan2(_y2 - _y1, _x2 - _x1)

    x1 = _x1
    y1 = _y1
    x2 = _x1 + math.cos(bearing) * side
    y2 = _y1 + math.sin(bearing) * side 

    if depth > 0:
        koch_snowflake(image, depth - 1, side, x1, y1, x2, y2)
    else:
        draw_line(image, x1, y1, x2, y2)

    x1 = x2
    y1 = y2
    x2 = x1 + math.cos(bearing + (math.pi / 3)) * side
    y2 = y1 + math.sin(bearing + (math.pi / 3)) * side

    if depth > 0:
        koch_snowflake(image, depth - 1, side, x1, y1, x2, y2)
    else:
        draw_line(image, x1, y1, x2, y2)

    x1 = x2
    y1 = y2
    x2 = x1 + math.cos(bearing - (math.pi / 3)) * side
    y2 = y1 + math.sin(bearing - (math.pi / 3)) * side

    if depth > 0:
        koch_snowflake(image, depth - 1, side, x1, y1, x2, y2)
    else:
        draw_line(image, x1, y1, x2, y2)

    x1 = x2
    y1 = y2
    x2 = x1 + math.cos(bearing) * side
    y2 = y1 + math.sin(bearing) * side

    if depth > 0:
        koch_snowflake(image, depth - 1, side, x1, y1, x2, y2)
    else:
        draw_line(image, x1, y1, x2, y2)
        
        


def start_koch_snowflake(image, depth):
    size = image.shape[0]
    height = size // (3 / 2)
    side = int((height / math.sqrt(3)) * 2)
    x_offset = (size - side) // 2
    y_offset = (size - height) // 4

    #Botttom side
    x1 = x_offset
    y1 = height + y_offset
    x2 = x1 + side
    y2 = y1
    koch_snowflake(image, depth, side, x1, y1, x2, y2)

    #Left side
    # x1 remains the same
    # y1 remains the same
    x2 = size // 2
    y2 = y_offset
    koch_snowflake(image, depth, side, x2, y2, x1, y1)

    #Right side
    x1 = x2
    y1 = y2
    x2 = side + x_offset
    y2 = height + y_offset
    koch_snowflake(image, depth, side, x2, y2, x1, y1)

    show_image(image)

base = cv2.imread('base.png')
start_koch_snowflake(base, 7)
