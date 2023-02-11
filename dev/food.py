import random

class Food:
  def __init__(self, canvas) -> None:
    x = random.randint(0, 900/30-1) * 30
    y = random.randint(0, 600/30-1) * 30
    self.coordinates = [x, y]
    canvas.create_oval(x, y, x+30, y+30, fill="#ff0000", tags="food")