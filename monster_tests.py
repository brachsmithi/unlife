import unittest
from monster import Monster

class MonsterTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 11
        self.y = 23
        self.monster = Monster(self.x, self.y)
        
    def testX(self):
        assert self.monster.x == self.x, 'wrong x position for monster'

    def testY(self):
        assert self.monster.y == self.y, 'wrong y position for monster'

    def testRadius(self):
        assert self.monster.radius == 5, 'wrong radius for monster'

    def testPosition(self):
        assert self.monster.position() == (self.x, self.y), 'wrong position for monster'

