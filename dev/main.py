from tkinter import *
from snake import Snake

#----------------------------------------------------------------------------------------#

def new_game():
  canvas.delete("all")
  my_snake = Snake(canvas)
  
  window.bind('<Left>', lambda event: my_snake.change_direction('left'))
  window.bind('<Right>', lambda event: my_snake.change_direction('right'))
  window.bind('<Up>', lambda event: my_snake.change_direction('up'))
  window.bind('<Down>', lambda event: my_snake.change_direction('down'))
  window.bind('<space>', lambda event: my_snake.press_space())
  window.bind('q', lambda event: quit(my_snake))
  window.bind('r', lambda event: restart(my_snake))

  my_snake.next_turn()

def quit(snake):
  if snake.end:
    print(snake.score)
    window.destroy()

def restart(snake):
  if snake.restart:
    new_game()

#------------------------------------------------------------------------------------------#

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

new_game()

window.mainloop()