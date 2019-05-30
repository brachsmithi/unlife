from human import Human

class Mover:

    def __init__(self, generator, width, height):
        self.generator = generator
        self.width = width
        self.height = height

    def describe(self):
        print('Mover')
        
    def move(self, entity, field_tracker):
        while True:
            new_position = self.generator.randomLocation(entity.position())
            if self.within_bounds(new_position) and self.available(new_position, field_tracker):
                break
        entity.x = new_position[0]
        entity.y = new_position[1]
        if type(entity) is Human:
            field_tracker.add_human(entity)
        else:
            field_tracker.add_monster(entity)

    def within_bounds(self, position):
        return position[0] >= 0 and position[0] < self.width and\
               position[1] >= 0 and position[1] < self.height

    def available(self, position, field_tracker):
        return not field_tracker.occupied(position)
