import tkinter 
import random


GAME_WIDTH = 900
GAME_HEIGHT = 600
SPEED = 50
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

class Snake:
  def __init__(self) -> None:
    self.body_size = BODY_PARTS
    self.coordinates = []
    self.squares = []

    for i in range(0, BODY_PARTS):
      self.coordinates.append([0, 0])

    for x, y in self.coordinates:
      square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
      self.squares.append(square)

class Food:
  def __init__(self) -> None:
    x = random.randint(0, GAME_WIDTH/SPACE_SIZE-1) * SPACE_SIZE
    y = random.randint(0, GAME_HEIGHT/SPACE_SIZE-1) * SPACE_SIZE
    self.coordinates = [x, y]
    canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tags="food")

def next_turn(snake, food):
  if space:
    window.wait_variable(pause)
    
  x, y = snake.coordinates[0]

  if direction == 'up':
    y -= SPACE_SIZE
  elif direction == 'down':
    y += SPACE_SIZE
  elif direction == 'left':
    x -= SPACE_SIZE
  elif direction == 'right':
    x += SPACE_SIZE

  snake.coordinates.insert(0, (x, y))
  square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
  snake.squares.insert(0, square)

  if x == food.coordinates[0] and y == food.coordinates[1]:
    global score
    score += 1
    label.config(text="Score={}".format(score))
    canvas.delete("food")
    food = Food()
  else:
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]


  if check_collisions(snake) or quit:
    game_over()
  else:
    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
  global direction

  if not space:
    if new_direction == 'left':
      if direction != 'right':
        direction = new_direction
    elif new_direction == 'right':
      if direction != 'left':
        direction = new_direction
    elif new_direction == 'up':
      if direction != 'down':
        direction = new_direction
    elif new_direction == 'down':
      if direction != 'up':
        direction = new_direction

def check_collisions(snake):
  x, y = snake.coordinates[0]
  if x < 0 or x >= GAME_WIDTH:
    return True
  elif y < 0 or y >= GAME_HEIGHT:
    return True

  for body_part in snake.coordinates[1:]:
    if x == body_part[0] and y == body_part[1]:
      print("GAME OVER")
      return True

  return False

def game_over():
  canvas.delete("all")
  canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, 
                     font=('consolas',70), text="GAME OVER", fill="red", tags="gameover")

def press_space():
  global space
  if space:
    space = False
  else:
    space = True
  if not space:
    pause.set(pause.get()+1)

def press_quit():
  global quit
  quit = True
  game_over()

window = tkinter.Tk()
window.title("Snake game")
window.resizable(False, False)

quit = False
space = False
pause = tkinter.IntVar()
score = 0
direction = 'down'
label = tkinter.Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()
canvas = tkinter.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

print(screen_width, "X", screen_height)
print(window_width, "X", window_height)

x = int((screen_width - window_width)/2)
y = int((screen_height - window_height)/4)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<space>', lambda event: press_space())
window.bind('q', lambda event: press_quit())

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()