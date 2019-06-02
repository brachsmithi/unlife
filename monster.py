from entity import Entity

class Monster(Entity):

    def __init__(self, x, y):
        Entity.__init__(self, x, y, 5)

    def describe(self):
        print('Monster at ' + str(self.x) + ', ' + str(self.y))
