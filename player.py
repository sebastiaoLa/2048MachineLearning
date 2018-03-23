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
    
    def play(self,count):
        return self.keys[self.dna.genes[count]]