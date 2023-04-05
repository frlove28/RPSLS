from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
          for gesture in self.gestures:
              print(gesture)
              
              
mark = Human("Mark")
mark.choose_gesture()
            
                    