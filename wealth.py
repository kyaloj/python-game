# The money
import random

class Wealth:
  def __init__(self, value):
    self.value = value

  def destroy(self):
    # Assumed to be in a wooden cart in the battle field
    # destroy by half or just an 8th.
    destruction = random.choice(['high', 'medium'])
    if destruction == 'high':
      self.value /= 2
    else:
      self.value /= 8
