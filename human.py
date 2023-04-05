from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        for gesture in self.gestures:
            print(gesture)
        
        self.choice = input('Please choose an attack from printed list: ')
        print (f"{self.name} chooses {self.choice}")
        
         
                

      
              
              
mark = Human("Mark")
mark.choose_gesture()
            
                    