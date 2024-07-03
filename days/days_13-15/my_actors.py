import random

class Creech:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def d_roll(self):
        roll = random.randint(1, 10)
        return roll * self.rating
    
class Reptile(Creech):
    def __init__(self, name, rating, color, is_magical):
        super().__init__(name, rating)
        self.color = color
        self.is_magical = is_magical

    def d_roll(self):
        roll = super().d_roll()
        value = roll * self.color
        if self.is_magical:
            value = value * 3

        return value
    
class Sorceror(Creech):

    def attack(self, creature):
        my_roll = self.d_roll()
        their_roll = creature.d_roll()

        return my_roll >= their_roll