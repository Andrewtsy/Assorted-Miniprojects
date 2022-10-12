"""This script is kind of a hack
It doesn't actually play Rock Paper Scissors,
But simply returns win, lose, tie based on pure random chance
Which then again, it just what Rock Paper Scissors is
Hopefully, it is a fun illustration of what shouldn't be done
While also exploring some basic coding concepts

Just for Fun :)
"""

import random

def main():
    print('Play and enter move: (Scissors, Paper, Rock) \nEnter Blank Value at any time to Quit')
    while True:
        # Assigns user input and random number from 0 to 1 to move and exp respectively
        move, exp = [input('Enter your throw: '), random.random()]
        # Checks if input is blank
        if move:
            # ~33% chance of each outcome occuring
            if exp > 0.66:
                print('You win!')
            elif 0.66 >= exp > 0.33:
                print('I win!')
            if exp < 0.33:
                print('It\'s a tie!')
        else:
            break
                
if __name__ == '__main__':
    main()