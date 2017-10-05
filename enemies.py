class Enemy:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage

  def is_alive(self):
    return self.hp > 0


class Slug(Enemy):
  def __init__(self):
    super().__init__(name="Slug", hp=3, damage=1)

class Spider(Enemy):
  def __init__(self)
    super().__init__(name="Spider", hp=5, damage=3)

class Parasite(Enemy):
  def __init__(self):
    super().__init__(name="Parasite", hp=10, damage=6)

class Goblin(Enemy):
  def __init__(self):
    super().__init__(name="Goblin", hp=17, damage=8)

class Ogre(Enemy):
  def __init__(self):
    super().__init__(name="Ogre", hp=35, damage=14)

class RedOgre(Enemy):
  def __init__(self):
    super().__init__(name="Red Ogre", hp=60, damage=20)
