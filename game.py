#Display welcome message // display rules of game
from human import Human
from ai import Ai
from player import Player
from time import sleep


class Game():
    def __init__(self):
        pass

    def welcome(self):
        sleep(1)
        print('Welcome to a wonderful game of chance!')
        print('Each player picks a gesture and reveals it at the same time. The winner is the one who gets 2 wins. In a tie, the process is repeated until a winner is found.')
        sleep(5)
        print('You can choose between Rock, Paper, Scissors, Lizard or Spock')
        sleep(3)
        print('Rock crushes Scissors')
        sleep(2)
        print('Scissors cuts Paper')
        sleep(2)
        print('Paper covers Rock')
        sleep(2)
        print('Rock crushes Lizard')
        sleep(2)
        print('Lizard poisons Spock')
        sleep(2)
        print('Spock smashes Scissors')
        sleep(2)
        print('Scissors decapitates Lizard')
        sleep(2)
        print('Lizard eats Paper')
        sleep(2)
        print('Paper disproves Spock')
        sleep(2)
        print('Spock vaporizes Rock')
        sleep(3)
        print('Now that you know the rules, lets get started!')
    #greeting_message = welcome()

    # def display_gesture_options(self): 
    #     print(self.gesture)
    # display_gesture = display_gesture_options()

    def run_game(self):
        self.welcome()
        self.game_select()
        while (self.player_one.player_score < 2 and self.player_two.player_score <2):
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.compare_gestures()
            self.display_winner()

    def display_winner(self):
        if (self.player_one.player_score == 2):
            print(f'{self.player_one.name} wins the game!')

        elif (self.player_two.player_score == 2):
            print(f'{self.player_two.name} wins the game!')
    def compare_gestures(self):
        
        if self.player_one.chosen_gesture == 'rock':
            if self.player_two.chosen_gesture == 'rock':
                print('It is a tie.')
            
            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.player_score += 1
                print(f'paper covers rock {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'scissors':
                self.player_one.player_score += 1
                print(f'rock crushes scissors {self.player_one.name} wins')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_one.player_score += 1
                print(f'rock crushes lizard {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_two.player_score +=1
                print(f'spock vaporizes rock {self.player_two.name} wins')
         
        if self.player_one.chosen_gesture == 'paper':
            if self.player_two.chosen_gesture == 'rock':
                self.player_one.player_score += 1
                print(f'paper covers rock {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'paper':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_two.player_score += 1
                print(f'scissors cut paper {self.player_two.name} wins')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_two.player_score += 1
                print(f'lizard eats paper {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_one.player_score += 1
                print(f'paper disproves spock {self.player_one.name} wins')
        
        # 3rd line
        if self.player_one.chosen_gesture == 'scissors':
            if self.player_two.chosen_gesture == 'rock':
                self.player_two.player_score += 1
                print(f'rock crushes scissors {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'scissors':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'paper':
                self.player_one.player_score += 1
                print(f'scissors cut paper {self.player_one.name} wins')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_one.player_score += 1
                print(f'scissors decapitates lizard {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_two.player_score += 1
                print(f'spock smashes scissors {self.player_two.name} wins')
        
        # 4th line
        if self.player_one.chosen_gesture == 'lizard':
            if self.player_two.chosen_gesture == 'rock':
                self.player_two.player_score += 1
                print(f'rock crushes lizard {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'lizard':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_two.player_score += 1
                print(f'scissors decapitates lizard {self.player_two.name} wins')

            elif self.player_two.chosen_gesture == 'paper':
                self.player_one.player_score += 1
                print(f'lizard eats paper {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_one.player_score += 1
                print(f'lizard poisons spock {self.player_one.name} wins')
        
        # 5th line
        if self.player_one.chosen_gesture == 'spock':
            if self.player_two.chosen_gesture == 'rock':
                self.player_one.player_score += 1
                print(f'spock vaporizes rock {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.player_score += 1
                print(f'paper disproves spock {self.player_two.name} wins')

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_one.player_score += 1
                print(f'spock smashes scissors {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'lizard':
                self.player_two.player_score += 1
                print(f'lizard poisons spock {self.player_two.name} wins')
        
        

        






            

    def game_select(self):
        print("Please select single Press 1, or multiplayer press 2")
        self.game_mode = input("")


        if self.game_mode == "1":
            print("You have selected singleplayer.")
            self.player_one = Human() 
            self.player_two = Ai() 
            
        
        elif self.game_mode == "2":
            print("You have selected Multiplayer")
            self.player_one = Human() 
            self.player_two = Human() 
            

        else:
            print("You have not selected a proper game mode")
            self.game_select()
