# square(center, side, depth):
#   draw a square of side length side centered at point center
#   if depth > 0:
#       determine four points side units from center in each direction
#       call square at each of these with depth decremented by 1

import cv2

frame=cv2.imread('base.png')

def square(x, y, side, depth):
    s = side // 2
    top_left = (x - s, y - s)
    # top_right = (x + s, y - s)
    # bot_left = (x - s, y + s)
    bot_right = (x + s, y + s)
    
    colour = (depth*50, 100, (depth*50)/2)
    cv2.rectangle(frame, top_left, bot_right, colour, -1) # if final value (thickness) is < 0, square will be filled


    cv2.imshow('square',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        quit()
        
    if depth > 0:
        new_side = side // 3
        square(x - side, y - side, new_side, depth - 1) # Top Left
        square(x, y - side, new_side, depth - 1) # Top
        square(x + side, y - side, new_side, depth - 1) # Top Right
        square(x + side, y, new_side, depth - 1) # Right
        square(x + side, y + side, new_side, depth - 1)# Bot Right
        square(x, y + side, new_side, depth - 1) # Bottom
        square(x - side, y + side, new_side, depth - 1) # Bot Left
        square(x - side, y, new_side, depth - 1) # Left

square(499, 499, 333, 5) # indexed from 0
while True:
    cv2.imshow('square', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        quit()
