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
        
    def testMonsterLocationInRange_outsideRange(self):
        tracker = self.tracker
        tracker.add_monster(Monster(50, 50))
        assert not tracker.monster_location_in_range((40, 60), 10)
        assert not tracker.monster_location_in_range((60, 40), 10)
        assert not tracker.monster_location_in_range((60, 60), 10)
        assert not tracker.monster_location_in_range((40, 40), 10)

    def testMonsterLocationInRange_inRange_Higher(self):
        tracker = self.tracker
        tracker.add_monster(Monster(30, 30))
        assert tracker.monster_location_in_range((21, 21), 10) == (30, 30)
        
    def testMonsterLocationInRange_inRange_Lower(self):
        tracker = self.tracker
        tracker.add_monster(Monster(10, 10))
        assert tracker.monster_location_in_range((19, 19), 10) == (10, 10)

    def testHumanLocationInRange_outsideRange(self):
        tracker = self.tracker
        tracker.add_human(Human(50, 50))
        assert not tracker.human_location_in_range((45, 55), 5)
        assert not tracker.human_location_in_range((55, 45), 5)
        assert not tracker.human_location_in_range((55, 55), 5)
        assert not tracker.human_location_in_range((45, 45), 5)

    def testHumanLocationInRange_inRange_Higher(self):
        tracker = self.tracker
        tracker.add_human(Human(30, 30))
        assert tracker.human_location_in_range((26, 26), 5) == (30, 30)
        
    def testHumanLocationInRange_inRange_Lower(self):
        tracker = self.tracker
        tracker.add_human(Human(10, 10))
        assert tracker.human_location_in_range((14, 14), 5) == (10, 10)


        # TODO return closest!
        
        
        
