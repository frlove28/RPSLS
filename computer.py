import random 


class Computer:
    def __init__(self, name):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.score =0
        self.choice = ""
        
        
        
    
    def choose_gesture(self):
        self.gestures = random.choice(self.gestures)
        self.choice = self.gestures



    def is_winner(self):
        return self.score >= 2

print(self.gestures)