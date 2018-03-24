import random

from player import Player
from constants import PLAYERTOTAL
import shelve
import os.path

class Population(object):

    def __init__(self):
        if os.path.isfile('previousPop.shelve'):
            print 'Using previous population'
            slv = shelve.open('previousPop.shelve')
            self.population = slv['population']
            self.genCount = slv['genNumber']
            slv.close()
        else:
            self.population = []
            for i in range(0,PLAYERTOTAL):
                self.population.append(Player())
            self.genCount = 0
        self.actualPlayer = 0
        
        
    def play(self):

        return self.population[self.actualPlayer].play()

    def set_fitness(self,fitness,modifier):
        self.modifier = modifier
        self.population[self.actualPlayer].fitness = fitness
        self.next_player()

    def calcFitness(self):
        maxFitness = 0
        for i in self.population:
            if i.fitness > maxFitness:
                maxFitness = i.fitness
        
        for i in self.population:
            i.fitness = float(i.fitness)/maxFitness

    def gen_matingpool(self):
        self.calcFitness()
        self.matingpool = []
        print ''
        print 'fitness: '
        for i in self.population:
            print self.population.index(i),' ',int(i.fitness*100)*self.modifier,
            if i.fitness*100 > 30:
                self.matingpool += [i.dna]*int(i.fitness*100)*self.modifier
                print ''
            else:
                print 'dead'


    def newGen(self):
        self.gen_matingpool()
        for i in range(0,PLAYERTOTAL):
            partnerA = random.choice(self.matingpool)
            partnerB = random.choice(self.matingpool)
            child = partnerA.crossover(partnerB)
            self.population[i] = Player(child)
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
        if self.actualPlayer<PLAYERTOTAL-1:
            self.actualPlayer += 1
        else:
            self.newGen()

        