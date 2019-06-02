import unittest
from human_tests import HumanTestCase
from monster_tests import MonsterTestCase
from mover_tests import MoverTestCase
from field_tracker_tests import FieldTrackerTestCase
from motion_generator_tests import MotionGeneratorTestCase
       
runner = unittest.TextTestRunner()
suite1 = unittest.makeSuite(FieldTrackerTestCase, 'test')
suite2 = unittest.makeSuite(HumanTestCase, 'test')
suite3 = unittest.makeSuite(MonsterTestCase, 'test')
suite4 = unittest.makeSuite(MoverTestCase, 'test')
suite5 = unittest.makeSuite(MotionGeneratorTestCase, 'test')
all = unittest.TestSuite((suite1, suite2, suite3, suite4, suite5))

runner.run(all)
