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
