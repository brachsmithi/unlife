import unittest
from human import Human
from monster import Monster
from mover import Mover
from random_motion_generator import RandomMotionGenerator
from field_tracker import FieldTracker

class MockRandomMotionGenerator(RandomMotionGenerator):
    def __init__(self):
        self.loc = []
        self.i = 0
        
    def randomLocation(self, location):
        new_loc = self.loc[self.i]
        self.i += 1
        return new_loc
    
class MoverTestCase(unittest.TestCase):

    def setUp(self):
        self.x = 11
        self.y = 23
        self.width = 40
        self.height = 30
        self.generator = MockRandomMotionGenerator()
        self.field_tracker = FieldTracker()
        self.human = Human(self.x, self.y)
        self.field_tracker.add_human(self.human)
        self.mover = Mover(self.generator, self.width, self.height)
    
    def testMove_noRestrictions(self):
        location = (2, 10)
        tracker = FieldTracker()
        self.generator.loc.append(location)
        self.mover.move(self.human, self.field_tracker, tracker)
        assert location == self.human.position()
        assert self.human in tracker.humans

    def testMove_noRestrictions(self):
        monster = Monster(self.x, self.y)
        location = (self.x - 1, self.y + 1)
        tracker = FieldTracker()
        self.generator.loc.append(location)
        self.mover.move(monster, self.field_tracker, tracker)
        assert location == monster.position()
        assert monster in tracker.monsters      

    def testMove_doesNotCrossLeftEdge(self):
        self.human.x = 0
        tracker = FieldTracker()
        self.generator.loc.append((-1, self.y))
        location = (0, self.y + 1)
        self.generator.loc.append(location)
        self.mover.move(self.human, self.field_tracker, tracker)
        assert location == self.human.position()
        assert self.human in tracker.humans       
        
    def testMove_doesNotCrossRightEdge(self):
        self.human.x = self.width - 1
        tracker = FieldTracker()
        self.generator.loc.append((self.width, self.y))
        location = (self.width - 1, self.y + 1)
        self.generator.loc.append(location)
        self.mover.move(self.human, self.field_tracker, tracker)
        assert location == self.human.position()
        assert self.human in tracker.humans       

    def testMove_doesNotCrossTopEdge(self):
        self.human.y = 0
        tracker = FieldTracker()
        self.generator.loc.append((self.x, -1))
        location = (self.x + 1, 0)
        self.generator.loc.append(location)
        self.mover.move(self.human, self.field_tracker, tracker)
        assert location == self.human.position()
        assert self.human in tracker.humans       

    def testMove_doesNotCrossBottomEdge(self):
        self.human.y = self.height - 1
        tracker = FieldTracker()
        self.generator.loc.append((self.x, self.height))
        location = (self.x, self.height - 1)
        self.generator.loc.append(location)
        self.mover.move(self.human, self.field_tracker, tracker)
        assert location == self.human.position()
        assert self.human in tracker.humans       

    def testMove_doesNotAllowTwoOccupantsInPosition(self):
        human2 = Human(self.x, self.y + 1)
        tracker = FieldTracker()
        location1 = (self.x + 1, self.y)
        location2 = (self.x + 1, self.y + 2)
        self.generator.loc.append(location1)
        self.generator.loc.append(location1)
        self.generator.loc.append(location2)
        self.mover.move(self.human, self.field_tracker, tracker)
        self.mover.move(human2, self.field_tracker, tracker)
        assert location2 == human2.position()
        assert self.human in tracker.humans       
        assert human2 in tracker.humans       

    def testMove_humanDoesNotApproachDetectedMonster(self):
        monster = Monster(self.x + 9, self.y - 9)
        self.field_tracker.add_monster(monster)
        location = (self.x, self.y + 1)
        self.generator.loc.append((self.x + 1, self.y - 1))
        self.generator.loc.append((self.x + 1, self.y))
        self.generator.loc.append((self.x, self.y - 1))
        self.generator.loc.append(location)
        new_tracker = FieldTracker()
        self.mover.move(self.human, self.field_tracker, new_tracker)
        assert location == self.human.position()
        assert self.human in self.field_tracker.humans

        
