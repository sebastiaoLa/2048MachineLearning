import random
from constants import LIFESPAN,MUTATIONCHANCE,GENES

class Dna(object):
    def __init__(self,genes = None):
        if genes:
            self.genes = genes
        else:
            self.genes = range(0,LIFESPAN)
            for i in range(0,LIFESPAN):
                self.genes[i] = random.randint(0,GENES)
    
    def crossover(self,partner):
        mid = random.randint(0,len(self.genes)-1)
        child = range(0,len(self.genes))
        for i in range(0,len(self.genes)):
            if random.randint(0,100)/float(100)<=MUTATIONCHANCE:
                child[i] = random.randint(0,GENES)
            else:
                if i<mid:
                    child[i] = self.genes[i]
                else:
                    child[i] = partner.genes[i]
        return Dna(child)
                


    