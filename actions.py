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
