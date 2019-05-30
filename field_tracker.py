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
