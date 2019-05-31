from human import Human
from monster import Monster

class Mover:

    def __init__(self, generator, width, height):
        self.generator = generator
        self.width = width
        self.height = height

    def describe(self):
        print('Mover')
        
    def move(self, entity, old_field_tracker, new_field_tracker):
        while True:
            new_position = self.generator.randomLocation(entity.position())
            if self.within_bounds(new_position) and\
               not self.moving_toward_monster(entity, new_position, old_field_tracker) and\
               self.available(new_position, new_field_tracker):
                break
        entity.x = new_position[0]
        entity.y = new_position[1]
        if type(entity) is Human:
            new_field_tracker.add_human(entity)
        else:
            new_field_tracker.add_monster(entity)

    def within_bounds(self, position):
        return position[0] >= 0 and position[0] < self.width and\
               position[1] >= 0 and position[1] < self.height

    def available(self, position, field_tracker):
        return not field_tracker.occupied(position)

    def moving_toward_monster(self, entity, position, field_tracker):
        if type(entity) is Monster:
            return False
        monster_loc = field_tracker.monster_location_in_range(entity.position(), 10)
        if not monster_loc:
            return False
        old_diff_x = abs(monster_loc[0] - entity.position()[0])
        new_diff_x = abs(monster_loc[0] - position[0])
        old_diff_y = abs(monster_loc[1] - entity.position()[1])
        new_diff_y = abs(monster_loc[1] - position[1])
        return old_diff_x >= new_diff_x and old_diff_y >= new_diff_y
