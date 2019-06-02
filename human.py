from entity import Entity

class Human(Entity):

    def __init__(self, x, y):
        Entity.__init__(self, x, y, 10)

    def describe(self):
        print('Human at ' + str(self.x) + ', ' + str(self.y))
