from kingdom import Kingdom
from king import King
from wealth import Wealth
from trebuchet import Trebuchet

# The war zone
class Battle:
  def __init__(self):
    print('')
    print("#" * 100)

    print(
      """ 

      Welcome to game of thrones. Attack your opponent Kingdom known
      as supermen.kill all soldiers and capture king.Once all soldiers are dead,
      you will capture king automatically and win.      

      """
    )
    print("#" * 100)
    print('')


  def launch(self):
    self.setup_battle_field()
    self.run_battle()
    self.print_results()

  def setup_battle_field(self):
    name = input('What name do you want for your kingdom?: ').strip()
    if not name:
      print('Name is required')
      return

    self.attacking_kingdom = self.mighty_kingdom = Kingdom({
      'name': name,
      'king': King('mighty King'),
      'soldiers': 10,
      'wealth': Wealth(1_000_000)
      
    })

    self.recieving_kingdom = self.opponent = Kingdom(
      {
        'name': 'supermen',
        'king': King('super King'),
        'soldiers': 10,
        'wealth': Wealth(1_000_000)
      }
    )
    self.weapon = Trebuchet()
    print('')

  def run_battle(self):
    while self.attacking_kingdom.wealth.value > 1:
      print('')
      print(f"{self.attacking_kingdom.name} attacks {self.recieving_kingdom.name}")
      self.attacking_kingdom.attack(opponent = self.recieving_kingdom, weapon = self.weapon)

      if not self.recieving_kingdom.king.in_battle():
        break # stop game once king captured

      self.attacking_kingdom, self.recieving_kingdom = self.recieving_kingdom, self.attacking_kingdom

  def print_results(self):
    print('')
    print('=' * 35)
    print('')

    for kingdom in [self.mighty_kingdom, self.opponent]:
      print(f"{kingdom.name.upper()} STATUS")
      print(kingdom.status())
      print('')

    print(f"{self.winner().upper()} WON THE BATTLE")
    print('=' * 35)
    print('')

  def winner(self):
    if self.mighty_kingdom.king.in_battle():
      return self.mighty_kingdom.name
    elif self.opponent.king.in_battle():
      return self.opponent.name
    else:
      return 'None'

Battle().launch()
