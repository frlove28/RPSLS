class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.score =0
        self.choice =  ['rock', 'paper', 'scissors', 'lizard', 'spock']
        
        
        
    
    def choose_gesture(self):
        pass

    
    def is_winner(self):
        return self.score >= 2
    pass
    
    
    