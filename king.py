class King:
  def __init__(self, name):
    self.name = name
    self.state = 'attacking'

  def capture(self):
    self.state = 'captured'

  def in_battle(self):
    return self.state == 'attacking'
