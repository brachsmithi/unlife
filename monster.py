class Monster:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10

    def describe(self):
        print('Monster at ' + str(self.x) + ', ' + str(self.y))

    def position(self):
        return (self.x, self.y)
