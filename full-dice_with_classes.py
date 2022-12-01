# CSE 210 W02 ASSIGNMENT:full-dice is a game where the player
# seeks to earn as many points as possible.
# Author: David Antonio Fajardo.
"""Rules of the game:
Dice is a game in which the player seeks to earn as many points as possible
by repeatedly rolling five dice and accumulating the score
until they are no longer able to continue.
When asked 'Roll dice? If the player answers "n" or no, the game is over.
If the player answers "y" or yes, the points are added to their score.
The player scores 100 points for each one that is rolled.
The player scores 50 points for each five that is rolled.
The dice values and player score are displayed on the screen.
If the player does not roll any ones or fives the game is over.' """
import random

class Die:

    def __init__(self):
        """Start the game!"""
        self.rolling()

    def rolling(self):
        self.rolled_numbers = []
        self.i = 0
        for self.i in range(5):
            value = random.randint(1,6)
            self.rolled_numbers.append(value)
        print(f'You rolled: {str(self.rolled_numbers)[1:-1]}')
class Score (Die):

    def __init__(self):
        """Instanciate the score"""
        self.score = 0
        self.inst= Die()
        self.points()

    def points(self):

        for number in (self.inst.rolled_numbers):
            if number == 1:
                self.score = self.score + 100
            elif number == 5:
                self.score = self.score + 50
        print(f'Your score is {self.score}')

        if self.score == 0:
            print(f'Game over!')
            exit()
        main()
def main():
    start = input(f'Roll dice? [y/n] ').lower()
    if start == 'y' or start == 'yes':
        Die()
        Score()
    elif start =='n' or start == 'no':
        print(f'Game finished!')
        exit()
if __name__=="__main__":
        main()