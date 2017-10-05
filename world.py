
# This module created a _world dictionary and parses the information given to it

_world = {}
starting_position = (0, 0)

def load_tiles():
  """Parses a file that describes the world space into the _world object"""
  with open('resources/map.txt', 'r') as f:
    row = f.readlines()
  x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
  for y in range(len(rows)):
    cols = rows[y].split('\t')
    for x in range(x_max):
      tile_name = cols[x].replace('\n', '')
      if tile_name == 'StartingRoom':
        global starting_position
        starting_position = (x, y)
      world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

# world[(x, y)] creats a key consisting of a co-ordinate pair x and y
# if the co-ordinate pair is blank no data is stored, otherwise the code
# looks into the tiles.py file and gets the tile whole name matches and
# passes the x and y co-ordinates to that tiles constructor

def tile_exists(x, y):
  return world.get((x, y))
