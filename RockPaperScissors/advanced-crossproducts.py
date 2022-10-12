"""Interesting approach to Rock Paper Scissors
This requires a little bit of knowledge of vectors in math
It takes the cross product of unit vectors
i: <1, 0, 0>, j: <0, 1, 0>, k: <0, 0, 1>
Which returns 0, negative, or positive unit vectors depending on their order
Takes a more unique approach that hopefully showcases there are many ways to do something!
"""

import random
import math
import numpy as np

class RockPaperScissor():
    def __init__(self):
        # Represents each throw as i, j, or k unit vectors
        self.book = {'Scissors': np.array([1, 0, 0]), 'Paper': np.array([0, 1, 0]), 'Rock': np.array([0, 0, 1])}
        print('Play and enter move: (Scissors, Paper, Rock) \nEnter Blank Value at any time to Quit')

    def vectortothrow(self, arr):
        # Converts vector to throw
        # We iterate through the dictionary and calculate the dot product of each item with the input arr
        # Whichever output is 1 means the item and arr match, and we output the associated throw
        for k, v in self.book.items():
            if np.dot(v, arr) == 1:
                return k

    def throwtovector(self, throw):
        # Converts throw to vector
        # Simply returns the value from the key in the book dictionary
        play = self.book[throw]
        return play

    def play(self, move):
        # Converts player's move from a throw to a vector
        play = self.throwtovector(move)
        # Randomly selects the opponent's move (as a vector)
        opp = random.choice([np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])])
        # Takes cross product
        res = np.cross(play, opp)
        # Converts opponent's move from vector to throw
        opp = self.vectortothrow(opp)
        # If the cross product has a positive value, player wins
        if max(res) == 1:
            print(f'I chose {opp}, you win!')
        # If the cross product has a negative value, opponent wins
        elif min(res) == -1:
            print(f'I chose {opp}, I win!')
        # If the cross product is 0, it's a tie
        else:
            print(f'I chose {opp}, It\'s a tie!')
            
def main():
    # Creates instance of RockPaperScissor Class
    game = RockPaperScissor()
    while True:
        move = input('Enter your throw: ')
        # Checks if input is blank
        if move:
            # Checks if move is valid
            if move in game.book.keys():
                game.play(move)
            else:
                print('Invalid throw, please try again')
        else:
            break
            
if __name__ == '__main__':
    main()