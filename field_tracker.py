from human import Human

class FieldTracker:

    def __init__(self):
        self.humans = []
        self.monsters = []

    def description(self):
        print('FieldTracker')

    def add_human(self, human):
        self.humans.append(human)

    def add_monster(self, monster):
        self.monsters.append(monster)

    def occupied(self, position):
        for human in self.humans:
            if human.position() == position:
                return True
        for monster in self.monsters:
            if monster.position() == position:
                return True
        return False

    def monster_location_in_range(self, position, radius):
        for monster in self.monsters:
            if abs(monster.position()[0] - position[0]) < radius and\
               abs(monster.position()[1] - position[1]) < radius:
                return monster.position()
        return None

    def human_location_in_range(self, position, radius):
        for human in self.humans:
            if abs(human.position()[0] - position[0]) < radius and\
               abs(human.position()[1] - position[1]) < radius:
                return human.position()
        return None
