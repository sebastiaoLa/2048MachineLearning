import random

from dna import Dna
from player import Player
from perceptron import Perceptron
from constants import PLAYERTOTAL
import shelve
import os.path


class Population(object):

    def __init__(self):
        if os.path.isfile('previousPop.shelve'):
        # if False:
            print 'Using previous population'
            slv = shelve.open('previousPop.shelve')
            if len(slv['population']) < PLAYERTOTAL:
                print 'discarting population'
                self.population = []
                for i in range(0, PLAYERTOTAL):
                    self.population.append(Player())
                self.genCount = 0
            else:
                self.population = slv['population']
                self.genCount = slv['genNumber']
            slv.close()
        else:
            self.population = []
            for i in range(0, PLAYERTOTAL):
                self.population.append(Player())
            self.genCount = 0
        self.actualPlayer = 0
        self.matingpool = []

    def play(self, inputs):
        return self.population[self.actualPlayer].play(inputs)

    def set_fitness(self, fitness):
        self.population[self.actualPlayer].fitness = fitness
        self.next_player()

    def get_best(self):
        player = None
        max_fitness = 0
        for i in self.population:
            if player is not None:
                if i.fitness > max_fitness:
                    max_fitness = i.fitness
                    player = i
            else:
                player = i
        return i

    def gen_matingpool(self):
        player = self.get_best()
        self.matingpool = [
            (i.neurons[0].dna.mutate(Dna()),
             i.neurons[1].dna.mutate(Dna())) for i in self.population]

    def newGen(self):
        self.gen_matingpool()
        for i in range(0, PLAYERTOTAL):
            perceptrons = []
            for j in range(0, 2):
                perceptrons.append(Perceptron(self.matingpool[i][j]))
            self.population[i] = Player(perceptrons)

        self.genCount += 1
        self.actualPlayer = 0
        print ''
        print 'saving pop'
        slv = shelve.open('previousPop.shelve')
        slv['population'] = self.population
        slv['genNumber'] = self.genCount
        slv.close()
        print "--- new GEN ---"
        print self.genCount

    def next_player(self):
        if self.actualPlayer < PLAYERTOTAL-1:
            self.actualPlayer += 1
        else:
            self.newGen()
