from robotcoin import start_max_coins_dynamic_path, make_board
from sys import argv
import turtle

if len(argv) > 1:
    size = int(argv[1])
else:
    size = 10

board = make_board(size)
cell_size = 600 // size

def coords_to_board(x, y):
    return -300 + (x * cell_size) + (cell_size // 2), 300 - (y * cell_size) - (cell_size // 2)

turtle.hideturtle()
turtle.tracer(0) # No animations
# turtle.speed(0)
turtle.pensize(5)
turtle.penup()
for i in range(-300, 301, cell_size): # Draw grid
    turtle.setpos(i, 300) # Vertical line
    turtle.pendown()
    turtle.setpos(i, -300)
    turtle.penup()
    turtle.setpos(-300, i) # Horizontal line
    turtle.pendown()
    turtle.setpos(300, i)
    turtle.penup()

for y, row in enumerate(board):
    for x, cell in enumerate(row):
        if cell == 1: # 1 means coin
            turtle.setpos(coords_to_board(x, y))
            turtle.dot(cell_size // 2, "red") # Place coins

values, path = start_max_coins_dynamic_path(board) # Run algorithm on board
font = "Arial", cell_size // 4, "bold"
for v in values:
    x = v[0]
    y = v[1]
    turtle.setpos(-300 + (x * cell_size) + (cell_size // 2) + (font[1] // 7), 300 - (y * cell_size) - (cell_size // 2) - int(0.8 * font[1])) # Offsets to allow for quirks of text
    turtle.write(values[v][0], align = "center", font = font)

turtle.showturtle()
turtle.tracer(1)
turtle.pencolor("green")
turtle.speed(2)
path = reversed(path)
for x, y in path:
    turtle.setpos(coords_to_board(x, y)) # Move through each point in turn
    turtle.pendown()

while True:
    pass
