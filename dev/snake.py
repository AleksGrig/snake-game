from tkinter import BooleanVar
from colors import color_list
from food import Food

class Snake:
  def __init__(self, canvas) -> None:
    self.coordinates = [(420, 60), (420, 30), (420, 0)]
    self.squares = []
    self.speed = 50
    self.pause = BooleanVar()
    self.pause.set(False)
    self.direction = 'down'
    self.color = 0
    self.canvas = canvas
    self.score = 0
    self.end = False
    self.restart = False
    self.text_id = self.canvas.create_text(20, 20, 
                                           fill="white",
                                           font=('Helvetica','20'), 
                                           text="{}".format(self.score), 
                                           tags="score")
    self.draw()


  def draw(self):
    for x, y in self.coordinates:
      square = self.canvas.create_rectangle(x, y, x+30, y+30, fill=color_list[self.color])
      self.color += 1
      self.squares.append(square)

  def change_direction(self,new_direction):
    if not self.pause.get():
      if new_direction == 'left':
        if self.direction != 'right':
          self.direction = new_direction
      elif new_direction == 'right':
        if self.direction != 'left':
          self.direction = new_direction
      elif new_direction == 'up':
        if self.direction != 'down':
          self.direction = new_direction
      elif new_direction == 'down':
        if self.direction != 'up':
          self.direction = new_direction

  def next_turn(self, food):
    if self.pause.get():
      self.canvas.wait_variable(self.pause)
    
    x, y = self.coordinates[0]

    if self.direction == 'up':
      y -= 30
    elif self.direction == 'down':
      y += 30
    elif self.direction == 'left':
      x -= 30
    elif self.direction == 'right':
      x += 30

    self.coordinates.insert(0, (x, y))
    if self.color == (len(color_list)):
      self.color = 0
    square = self.canvas.create_rectangle(x, y, x+30, y+30, fill=color_list[self.color])
    self.color += 1
    self.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
      self.score += 1
      self.canvas.delete("score")
      self.text_id = self.canvas.create_text(20, 20, 
                                             fill="white",
                                             font=('Helvetica','20'), 
                                             text="{}".format(self.score), 
                                             tags="score")
      self.canvas.delete("food")
      food = Food(self.canvas)
      self.speed -= 1
    else:
      del self.coordinates[-1]
      self.canvas.delete(self.squares[-1])
      del self.squares[-1]

    if self.check_collisions():
      self.game_over()
    else:
      self.canvas.after(self.speed, self.next_turn, food)

  def check_collisions(self):
    x, y = self.coordinates[0]
    if x < 0 or x >= 900:
      return True
    elif y < 0 or y >= 600:
      return True

    for body_part in self.coordinates[1:]:
      if x == body_part[0] and y == body_part[1]:
        return True

    return False

  def press_space(self):
    self.pause.set(not self.pause.get())

  def game_over(self):
    self.canvas.delete("all")
    self.canvas.create_text(self.canvas.winfo_width()/2, 40, 
                            font=('consolas',30), 
                            text="GAME OVER, your score: {}".format(self.score), 
                            fill="red", 
                            tags="gameover")
    self.canvas.create_text(self.canvas.winfo_width()/2, 80, 
                            font=('consolas',20), 
                            text="Press 'q' to quit".format(self.score), 
                            fill="grey", 
                            tags="quit")
    self.canvas.create_text(self.canvas.winfo_width()/2, 120, 
                            font=('consolas',20), 
                            text="Press 'r' to restart".format(self.score), 
                            fill="grey", 
                            tags="quit")
    self.end = True
    self.restart = True