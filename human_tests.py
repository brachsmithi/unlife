import unittest
from human import Human

class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 11
        self.y = 23
        self.human = Human(self.x, self.y)
        
    def testX(self):
        assert self.human.x == self.x, 'wrong x position for human'

    def testY(self):
        assert self.human.y == self.y, 'wrong y position for human'

    def testRadius(self):
        assert self.human.radius == 10, 'wrong radius for human'

    def testPosition(self):
        assert self.human.position() == (self.x, self.y), 'wrong position for human'

