import random

class MotionGenerator:

    def randomLocation(self, location):
        new_x = location[0] + random.randint(-1,1)
        new_y = location[1] + random.randint(-1,1)
        return (new_x, new_y)

    def move_toward(self, starting_location, destination):
        x = starting_location[0]
        y = starting_location[1]
        dest_x = destination[0]
        dest_y = destination[1]
        new_x = x
        new_y = y
        if x > dest_x:
            new_x = x - 1
        else:
            new_x = x + 1
        if y > dest_y:
            new_y = y - 1
        else:
            new_y = y + 1
        return (new_x, new_y)
