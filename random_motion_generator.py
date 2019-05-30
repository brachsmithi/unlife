import random

class RandomMotionGenerator:

    def randomLocation(self, location):
        new_x = location[0] + random.randint(-1,1)
        new_y = location[1] + random.randint(-1,1)
        return (new_x, new_y)
