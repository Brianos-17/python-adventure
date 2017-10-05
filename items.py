#!/usr/bin/python

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

class Gold(Item):
  def __init__(self, amt):
    self.amt = amt
    super().__init__(name="Gold", description="Shiny round coin. Worth {}".format(str(self.amt)),
      value=self.amt)

#Potion item which restores players health

class Potion(Item):
  def __init__(self):
    super().__init__(name="Potion", description="A bottle full of strange magical liquid",
      value=5)

# Weapon class which acts as a subclass of Item, but also extends its own subclasses

class Weapon(Item):
  def __init__(self, name, description, value, damage):
    self.damage = damage
    super().__init__(name, description, value)

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value,
      self.dagame)

class Stick(Weapon):
  def __init__(self):
    super().__init__(name="Stick", description="A small but firm branch, good for whacking", 
      value=0, damage=2)

class Rock(Weapon):
  def __init__(self):
    super().__init__(name="Rock", 
      decription="A small fist sized rock. You could hurt someone with that!",
      value=0, damage=5)

class RustyDagger(Weapon):
  def __init__(self):
    super().__init__(name="Rusty Dagger",
      description="An old rusted dagger, I hope you've had your tetanus shot!",
      value=2, damage=10)

class Dagger(Weapon):
  def __init__(self):
    super().__init__(name="Dagger",
      description="A small, yet effective, weapon. Way better than that stupid old Rusty Dagger",
      value=5, damage=15)

class Sword(Weapon):
  def __init__(self):
    super().__init__(name="Sword", description="A long sword, capable of slicing through anything!",
    value=10, damage=25)
