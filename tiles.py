#!/usr/bin/python

# MapTile class, provides a template for moving around the in-game world

import items, enemies

class MapTile:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def intro_text(self):
    raise NotImplementedError() # warns against the creation of an empty tile,
                                # tiles will be created from subclasses

  def modify_player(self, player):
    raise NotImplimentedError() # warns against the creation of an empty tile,
                                # tiles will be created from subclasses

class StartingRoom(MapTile):
  def intro_text(self):
    return """ Your head is pounding, your mouth is dry. You wake up on the floor of some dark
    cave with a torch flickering weakly on the wall. Where are you? How did you end up here?
    """

  def modify_player(self, player):
    #Room has no effect on player
    pass

#Provides a template for all Loot rooms

class LootRoom(MapTile):
  def __init__(self, x, y, item):
    self.item = item
    super().__init__(x, y)

  def add_loot(self, player):
    player.inventory.append(self.item)

  def modify_player(self, player):
    self.add_loot(player)

#Provides a template for all Enemy rooms

class EnemyRoom(MapTile):
  def __init__(self, x, y, enemy):
    self.enemy = enemy
    super().__init__(x, y)

  def modify_player(self, the_player):
    if self.enemy.is_alive(): # Player only has to fight if enemey is alive (can't respawn)
      the_player.hp = the_player.hp - self.enemy.damage
      print("{} hit you for {} damage. You have {} HP left.".format(self.enemy.name,
        self.enemy.damage, the_player.hp))

#Generates empty rooms for the player to walk through

class EmptyRoom(MapTile):
  def intro_text(self):
    return """This part of the cave is empty. Keep looking for the way out"""

  def modify_player(self, player):
    #Room has no effect on player
    pass

#Subclass of LootRoom, player finds 5 gold

class 5GoldRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Gold(5))

  def intro_text(self):
    return """There's somethinf sparkly on the floor. It's Gold!!"""

  def modifly_player(self, player):
    the_player.gold += 5
