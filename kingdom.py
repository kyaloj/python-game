# The awesome battalions
import random

class Kingdom:
  def __init__(self, args):
    self.name = args.get("name", None)
    self.king = args.get("king",None)
    self.soldiers = args.get("soldiers", None)
    self.wealth = args.get("wealth", None)

  def attack(self, opponent, weapon):
    weapon.fire()
    opponent.demolish()

  def demolish(self):
    self.wealth.destroy()
    # kill some soldiers
    for _ in range(random.randint(1, 4)):
      if self.soldiers > 0:
        self.soldiers -= 1

    if self.soldiers > 0:
      return

    self.king.capture()

  def status(self):
    print(f"King: {self.king.state}")
    print(f"Soldiers: {self.soldiers}")
    print(f"Wealth: {self.wealth.value} Gold Pieces")
    return ''
