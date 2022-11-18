from colors import color_list
import random

class Snake:
  def __init__(self, canvas) -> None:
    self.coordinates = [(420, 60), (420, 30), (420, 0)]
    self.squares = []
    self.speed = 50
    self.direction = 'down'
    self.color = 0
    self.canvas = canvas

  def draw(self):
    for x, y in self.coordinates:
      square = self.canvas.create_rectangle(x, y, x+30, y+30, fill=color_list[self.color])
      self.color += 1
      self.squares.append(square)

  def change_direction(self,new_direction):
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

  def game_over(self):
    self.canvas.delete("all")
    self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, 
                      font=('consolas',70), text="GAME OVER", fill="red", tags="gameover")

class Food:
  def __init__(self, canvas) -> None:
    x = random.randint(0, 900/30-1) * 30
    y = random.randint(0, 600/30-1) * 30
    self.coordinates = [x, y]
    canvas.create_oval(x, y, x+30, y+30, fill="#ff0000", tags="food")