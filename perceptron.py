from dna import Dna


class Perceptron(object):
    def __init__(self, dna):
        self.dna = dna if dna else Dna()
        self.weights = self.dna.genes
        self.fitness = 0

    def go(self, inputs):
        n = sum(self.execute(inputs))
        # print "INPUTS:", inputs
        return self.normalize(n)

    def execute(self, inputs):
        return [self.weights[i]*inputs[i] for i in range(0, len(inputs))]

    def normalize(self, n):
        if n < 0:
            return 0
        else:
            return 1
