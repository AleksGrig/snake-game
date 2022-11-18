from tkinter import *
from snake import *


window = Tk()
window.title("Snake game")
window.resizable(False, False)
canvas = Canvas(window, bg="#000000", height=600, width=900)
canvas.pack()
window.update()

my_snake = Snake(canvas)
my_snake.draw()
food = Food(canvas)

window.bind('<Left>', lambda event: my_snake.change_direction('left'))
window.bind('<Right>', lambda event: my_snake.change_direction('right'))
window.bind('<Up>', lambda event: my_snake.change_direction('up'))
window.bind('<Down>', lambda event: my_snake.change_direction('down'))

my_snake.next_turn(food)

window.mainloop()