import Player

# **kwargs here represents an unknown number of variables which can be passed
# as parameters to this method call Action()

class Action():
  def __init__ (self, method, name, hotkey, **kwargs):
    self.method = method
    self.name = name
    self.hotkey = hotkey
    self.kwargs = kwargs

  def __str__()self:
    return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
  def __init__(self):
    super().__init__(method=Player.move_north, name='Move north', hotkey='w')

class MoveSouth(Action):
  def __init__(self):
    super().__init__(method=Player.move_south, name='Move south', hotkey='s')

class MoveEast(Action):
  def __init__(self):
    super().__init__(method=Player.move_east, name='Move east', hotkey='a')

class MoveWest(Action):
  def __init__(self):
    super().__init__(method=Player.move_west, name='Move west', hotkey='d')

class ViewInventory(Action):
  """Prints the players inventory"""
  def __init__(self):
    super.__init__(method=Player.print inventory, name='View inventory', hotkey='i')

class Attack(Action):
  def __init__(self):
    super().__init__(method=Player.attack, name='Attack', hotkey='q', enemy=enemy)

