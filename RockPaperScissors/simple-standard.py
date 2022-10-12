"""A pretty basic, standard way to play Rock Paper Scissors
Goes through all of the possibilities one by one
"""

import random
import math

class RockPaperScissor():
    def __init__(self):
        self.book = ['Scissors', 'Paper', 'Rock']
        print('Play and enter move: (Scissors, Paper, Rock) \nEnter Blank Value at any time to Quit')

    def play(self, move):
        # Chooses a random throw for the opponent to give
        opp = random.choice(['Scissors', 'Paper', 'Rock'])
        # Goes through all possibilities
        if move == 'Scissors':
            if opp == 'Rock':
                print('I chose Rock, I win!')
            elif opp == 'Paper':
                print('I chose Paper, You win!')
            else:
                print('I chose Scissors, It\'s a tie!')
        elif move == 'Paper':
            if opp == 'Rock':
                print('I chose Rock, You win!')
            elif opp == 'Paper':
                print('I chose Paper, It\'s a tie!')
            else:
                print('I chose Scissors, I win!')
        elif move == 'Rock':
            if opp == 'Rock':
                print('I chose Rock, It\'s a tie!')
            elif opp == 'Paper':
                print('I chose Paper, I win!')
            else:
                print('I chose Scissors, You win!')
            
def main():
    # Creates instance of RockPaperScissor Class
    game = RockPaperScissor()
    while True:
        move = input('Enter your throw: ')
        # Checks if input is blank
        if move:
            # Checks if move is valid
            if move in game.book:
                game.play(move)
            else:
                print('Invalid throw, please try again')
        else:
            break
            
if __name__ == '__main__':
    main()