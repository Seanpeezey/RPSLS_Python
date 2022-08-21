from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input('please enter name ')

    def choose_gesture(self):
        
        self.chosen_gesture = self.gesture[0:4]
        user_input = (input('Pick a gesture '))
        user_input = user_input.lower()
        if user_input == self.gesture[0]:
            print('You chose rock!')
            self.chosen_gesture = self.gesture[0]
        
        elif user_input == self.gesture[1]:
            print('You chose paper!')
            self.chosen_gesture = self.gesture[1]

        elif user_input == self.gesture[2]:
            print('You chose scissors')
            self.chosen_gesture = self.gesture[2]

        elif user_input == self.gesture[3]:
            print ('You chose lizard!')
            self.chosen_gesture = self.gesture[3]

        elif user_input == self.gesture[4]:
            print ('You chose spock!')
            self.chosen_gesture = self.gesture[4]

        else:
            print('not a valid option try again')
        