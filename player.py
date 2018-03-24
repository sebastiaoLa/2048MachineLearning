from constants import LIFESPAN,GENES

import random

from dna import Dna
from selenium.webdriver.common.keys import Keys

class Player(object):
    def __init__(self,dna=None):
        if dna:
            self.dna = dna
        else:
            self.dna = Dna()
        self.keys = [
            Keys.UP,
            Keys.DOWN,
            Keys.LEFT,
            Keys.RIGHT
        ]
        
        self.fitness = 0
        self.count = -1
    
    def next_play(self):
        if self.count+1<len(self.dna.genes):
            self.count +=1 
        else:
            self.count = 0

    def play(self):
        self.next_play()
        try:
            move = self.keys[self.dna.genes[self.count]]
        except IndexError:
            self.count = 0
            move = self.keys[random.randint(0,GENES)]
        
        if move == Keys.UP:
            print 'UP ',
        elif move == Keys.DOWN:
            print 'DOWN ',
        elif move == Keys.LEFT:
            print 'LEFT ',
        elif move == Keys.RIGHT:
            print 'RIGHT ',
        return move