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

#Generates enemy rooms for each type of enemy

class SlugRoom(EnemyRoom):
  def __init__()self, x, y):
    super().__init__(x, y, enemies.Slug())

  def intro_text(self):
    if self.enemy.is_alive():
      return """A small slimy slug moves slowly towards you."""
    else:
      return """You see the slug you squished earlier on the ground."""

class SpiderRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Spider())

  def intro_text(self):
    if self.enemy.is_alive():
      return """A giant spider web blocks your path.
         Suddenly the spider jumps at you from above!"""
      else:
        return """The spiders lifeless body lies on the ground."""

class ParasiteRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Parasite())

  def intro_text(self):
    if self.enemy.is_alive():
      return """A gint blood sucking parasite detaches itself from a nearby carcus.
         \n It latches onto your leg."""
    else:
      return """The shrivelled up blood sucker is lying right where you left it."""

class GoblinRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Goblin())

  def intro_text(self):
    if self.enemy.is_alive():
      return """You hear a shriek of anger just before a Goblin jumps on your back!"""
    else:
      return """The dead Goblin is starting to smell..."""

class OgreRoom(EnemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.Ogre())

  def intro_text(self):
    if self.enemy.is_alive():
      return """Before you stands a giant ugle Ogre, and he looks mad!"""
    else:
      return """The body of the Ogre is blocking your path.
        \nIt's too heavy to move. You have to climb over it."""

class RedOgreRoom(enemyRoom):
  def __init__(self, x, y):
    super().__init__(x, y, enemies.RedOgre())

  def intro_text(self):
    if self.enemy.is_alive():
      return """You're so close! You can see the exit!
        \nBut standing in your way is the biggest Ogre you've ever seen.
        \nHe's gone red with rage... Good luck!"""
    else:
      return """That's it, you won, why are you going backwards?!"""

#Generates empty rooms for the player to walk through

class EmptyRoom(MapTile):
  def intro_text(self):
    return """This part of the cave is empty. Keep looking for the way out"""

  def modify_player(self, player):
    #Room has no effect on player
    pass

#Gives player a hint that they are going in the right direction

class HintRoom(MapTile):
  def intro_text(self):
    return """You feel a slight breeze. You must be going in the right direction"""

  def modify_player(self, player):
    #Room has no effect on player
    pass

#Subclasses of LootRoom, player finds gold, potions and weapons

class 5GoldRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Gold(5))

  def intro_text(self):
    return """There's something sparkly on the floor. It's 5 Gold!!"""

  def modifly_player(self, player):
    the_player.gold += 5

class 10GoldRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Gold(10))

  def intro_text(self):
    return """There's something sparkly on the floor. It's 10 Gold!!"""

  def modify_player(self, player):
    the_player.gold += 10

class PotionRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Potion())

  def intro_text(self):
    return """You've found an old chest. There's some sort of bottle inside.
      \nYou take a swig, it makes you feel better!"""

  def modify_player(self, player):
    the_player.hp += 15

class StickRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Stick())

  def intro_text(self):
    return """You find a stick on the ground. It could come in handy"""

class RockRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items,Rock())

  def intro_text(self):
    return """Theres a small rock on the ground, it might make a good weapon."""

class RustyDaggerRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.RustyDagger())

  def intro_text(self):
    return """Stuck in the ground is a small knife. Looks like its been there a while.
      \nIt's rusted with age."""

class DaggerRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Dagger())

  def intro_text(self):
    return """Youve stumbled across the body of another poor soul who got lost in this cave.
      \nBut at least he has a shiny new Dagger on his belt!"""

class SwordRoom(LootRoom):
  def __init__(self, x, y):
    super().__init__(x, y, items.Sword())

  def intro_text(self):
    return """There! In fromnt of you, stuck in a rock you can see the pommel of a might sword.
      \nWith a mighty effort you manage to pull the sword from the stone!"""
