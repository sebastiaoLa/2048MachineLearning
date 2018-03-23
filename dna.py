import random


class Dna(object):
    def __init__(self,genes = None):
        if genes:
            self.genes = genes
        else:
            self.genes = range(0,400)
            for i in range(0,400):
                self.genes[i] = random.randint(0,4)
    
    def crossover(self,partner):
        mid = range(0,len(self.genes))
        child = range(0,400)
        for i in range(0,len(self.genes)):
            if i<mid:
                child[i] = self.genes[i]
            else:
                child[i] = partner[i]
        return Dna(child)
                


    