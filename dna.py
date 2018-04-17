import random
from constants import INPUTS, MUTATIONCHANCE


class Dna(object):
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            self.genes = [random.uniform(-1, 1) for i in range(0, INPUTS)]

    def crossover(self, partner):
        mid = random.randint(int(len(self.genes)*0.30),
                             int(len(self.genes)*0.70))
        child = []
        for i in range(0, len(self.genes)):
            if random.random() <= MUTATIONCHANCE:
                child.append(random.uniform(-1, 1))
            else:
                if i < mid:
                    child.append(self.genes[i])
                else:
                    child.append(partner.genes[i])
        return Dna(child)

    def mutate(self, partner):
        for i in range(len(self.genes)):
            self.genes[i] = self.genes[i] + (partner.genes[i]*MUTATIONCHANCE)
        return self
