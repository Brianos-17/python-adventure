#!/usr/bin/python

import items

class Player():
  def __init__(self):
    self.iventory = [items.Gold(15)]
    self.hp = 100
    self.location_x, self.location_y = world.starting_position
    self.victory = False

  def is_alive(self): # Lets players know when they have died
    return self.hp > 0

  def print_inventory(self): # Iterates through inventory list and prints items
    for item in self.inventory:
      print(item, '\n')

# Movement methods for player

  def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    print(world.tile_exists(self.location_x, self.location_y).intro_text())

  def move_north(self):
    self.move(dx=0, dy=-1)

  def move_south(self):
    self.move(dx=0, dy=1)

  def move_east(self):
    self.move(dx=1, dy=0)

  def move_west(self):
    self.move(dx=-1, dy=0)

# Attacking methods

  def attack(self, enemy):
    bestWeapon = None
    max_dmg = 0
    for item in self.inventory:
      if isinstance(item, items.Weapon):
        if item.damage > max_dmg:
          max_dmg = item.damage
          best_weapon = item
    print("You use your {} against the {}!".format(best_weapon.name, enemy.name))
    enemy.hp -= best_weapon.damage
    if not enemy.is_alive():
      print("Congratulations, you slayed the {}!".format(enemy.name))
    else:
      print("You have dealt {} damage. {} health is down to {}!".format(max_dmg, enemy.name, enemy.hp))

#Method which allows player to execute an action

  def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
      action_method(**kwargs)

