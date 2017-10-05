class Item():
  """Base class of off which all items are built"""

# __init__ constructor called whenever a new item is created

  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value

# __str__ prints item object in a readable manner

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Gold item which acts as a subclass of the Item super class

class Gold(item):
  def __init__(self, amt):
    self.amt = amt
    super().__init__(name="Gold", description="Shiny round coin. Worth {}".format(str(self.amt)),
      value=self.amt)
