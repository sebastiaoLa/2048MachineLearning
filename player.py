from constants import INPUTS

import random

from dna import Dna
from selenium.webdriver.common.keys import Keys
from perceptron import Perceptron


class Player(object):
    def __init__(self, neurons=None):
        self.keys = [
            Keys.UP,
            Keys.DOWN,
            Keys.LEFT,
            Keys.RIGHT
        ]
        self.neurons = neurons if neurons else [
            Perceptron(Dna()), Perceptron(Dna())]

        self.fitness = 0

    def play(self, inputs):
        num = [x.go(inputs) for x in self.neurons]

        # print num
        if num == [0, 0]:
            move = Keys.LEFT
        elif num == [0, 1]:
            move = Keys.UP
        elif num == [1, 0]:
            move = Keys.DOWN
        else:
            move = Keys.RIGHT

        # if move == Keys.UP:
        #     print 'UP ',
        # elif move == Keys.DOWN:
        #     print 'DOWN ',
        # elif move == Keys.LEFT:
        #     print 'LEFT ',
        # elif move == Keys.RIGHT:
        #     print 'RIGHT ',
        return move
