from player import Player

class PopControl(object):
    def __init__(self):
        self.population = []
        for i in range(0,400):
            self.population.append(Player())
        self.actualPlayer = 0
        
    def play(self,count):
        self.actualPlayer = count
        return self.population[count].dna.genes

    def set_fitness(self,fitness):
        self.population[self.actualPlayer].fitness = fitness


        