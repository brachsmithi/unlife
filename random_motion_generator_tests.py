import unittest
from random_motion_generator import RandomMotionGenerator

class RandomMotionGeneratorTestCase(unittest.TestCase):

    def testRandomLocation(self):
        prev_x = 13
        prev_y = 34
        
        x_moved_left = False
        x_moved_right = False
        x_stayed_put = False
        y_moved_down = False
        y_moved_up = False
        y_stayed_put = False

        generator = RandomMotionGenerator()

        for i in range(0, 20):
            new_location = generator.randomLocation((prev_x, prev_y))
            if new_location[0] > prev_x:
                x_moved_right = True
            elif new_location[0] < prev_x:
                x_moved_left = True
            else:
                x_stayed_put = True
            if new_location[1] > prev_y:
                y_moved_down = True
            elif new_location[1] < prev_y:
                y_moved_up = True
            else:
                y_stayed_put = True
            
            assert self.stayedWithinOneSpace(new_location[0], prev_x), 'x moved out of range'
            assert self.stayedWithinOneSpace(new_location[1], prev_y), 'y moved out of range'
            prev_x, prev_y = new_location
        
        assert x_moved_right, 'human never moved right'
        assert x_moved_left, 'human never moved left'
        assert x_stayed_put, 'human never stayed put on x axis'
        assert y_moved_down, 'human never moved down'
        assert y_moved_up, 'human never moved up'
        assert y_stayed_put, 'human never stayed put on y axis'

    def stayedWithinOneSpace(self, new_point, old_point):
        return new_point >= old_point - 1 and new_point <= old_point + 1


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(RandomMotionGeneratorTestCase('testRandomLocation'))
        return suite
