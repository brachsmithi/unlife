class Entity:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def describe(self):
        print('Entity at ' + str(self.x) + ', ' + str(self.y))

    def position(self):
        return (self.x, self.y)
