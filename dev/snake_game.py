from tkinter import *
from snake import *


window = Tk()
window.title("Snake game")
window.resizable(False, False)

canvas = Canvas(window, bg="#000000", height=600, width=900)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window_width)/2)
y = int((screen_height - window_height)/4)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


my_snake = Snake(canvas)
my_snake.draw()
food = Food(canvas)

window.bind('<Left>', lambda event: my_snake.change_direction('left'))
window.bind('<Right>', lambda event: my_snake.change_direction('right'))
window.bind('<Up>', lambda event: my_snake.change_direction('up'))
window.bind('<Down>', lambda event: my_snake.change_direction('down'))
window.bind('<space>', lambda event: my_snake.press_space())

my_snake.next_turn(food)

window.mainloop()