import unittest
from field_tracker import FieldTracker
from human import Human
from monster import Monster

class FieldTrackerTestCase(unittest.TestCase):

    def setUp(self):
        self.tracker = FieldTracker()

    def testAddHuman(self):
        tracker = self.tracker
        human = Human(1, 2)
        tracker.add_human(human)
        assert human.position() == tracker.humans[0].position()

    def testAddMonster(self):
        tracker = self.tracker
        monster = Monster(4, 2)
        tracker.add_monster(monster)
        assert monster.position() == tracker.monsters[0].position()

    def testOccupied_Empty(self):
        tracker = self.tracker
        human = Human(10, 10)
        tracker.add_human(human)
        assert not tracker.occupied((1,1))

    def testOccupied_Filled(self):
        tracker = self.tracker
        human = Human(3, 4)
        tracker.add_human(human)
        assert tracker.occupied(human.position())

    def testOccupied_Monster(self):
        tracker = self.tracker
        monster = Monster(4, 8)
        tracker.add_monster(monster)
        assert tracker.occupied(monster.position())
        
