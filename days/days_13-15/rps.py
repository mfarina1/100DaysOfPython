import random

class Roll:
    def __init__(self, name):
        self.name = name

    def evaluate_roll(self, other_roll):
        if self.name == "rock":
            if other_roll.name == "scissors":
                print("you win!")
            else:
                return "you lose!"
            
        if self.name == "paper":
            if other_roll.name == "rock":
                return "you win!"
            else:
                return "you lose!"
            
        if self.name == "scissors":
            if other_roll.name == "paper":
                return "you win!"
            else:
                return "you lose!"
        
class Player:
    def __init__(self, name):
        self.name = name
        self.roll = None  # Will be assigned later