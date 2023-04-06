from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        for gesture in self.gestures:
            print(gesture)
        
        self.choice = input('Please choose an attack from printed list: ')
        print (f"{self.name} chooses {self.choice}")
        
         
                

    # def score_keeper(self):
    #     if self.score >= 2 :
    #         print (f"{self.name} wins!!!")

              
    # def store_user_choice(self):
    #     self.name = input()




player_one = Human()
player_two = Human()
player_one.choose_gesture()
            
                    