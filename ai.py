from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
    
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture)
        print(f'Mr.Roboto chose {self.chosen_gesture}')
        return self.chosen_gesture
        
    def player_name(self):
       self.name = 'Mr.Roboto'
