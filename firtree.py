class Firtree:

  def __init__(self):
    ...

  def of_stars(self):
    space = ' '
    star = '*'

    rows = int(input())
    spaces = rows-1
    stars = 1

    for i in range(rows):
      print((space * spaces) + (star * stars) + (space * spaces))
      stars += 2
      spaces -= 1

  def of_one_triangle(self):
    space = ' '
    star = '*'
    underscore = '_'
    slash = '/'
    backslash = '\\'

    if __name__ == "__main__":
      branches = int(input())
      spaces = branches - 1
      underscores = 1

      top = (space * branches) + star + (space * branches)
      trunk = (space * spaces) + "|_|" + (space * spaces)

      print(top)

      for i in range(branches):
        print((space * spaces) + slash + (underscore * underscores) + backslash + (space * spaces))
        underscores += 2
        spaces -= 1

      print(trunk)

  def of_triangles(self):
    space = ' '
    star = '*'
    underscore = '_'
    slash = '/'
    backslash = '\\'

    branches = int(input())
    spaces = branches - 0
    underscores = 3

    top = (space * (branches+1)) + star + (space * (branches+1))
    trunk = (space * spaces) + "|_|" + (space * spaces)

    print(top)

    for i in range(branches):
      print((space * spaces) + slash + (space * (underscores-2)) + backslash + (space * spaces))
      print((space * (spaces-1)) + slash + (underscore * underscores) + backslash + (space * (spaces-1)))
      underscores += 2
      spaces -= 1

    print(trunk)


firtree = Firtree()
firtree.of_stars()
firtree.of_one_triangle()
firtree.of_triangles()