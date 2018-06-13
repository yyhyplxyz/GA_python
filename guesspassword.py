import random
import unittest
import datetime
import sys
import statistics
import datetime
import time


geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "hello Yyh!"
def generateparent(length):
    genes = []
    while len(genes) < length:
        mysize = min(len(geneset), length - len(genes))
        genes.extend(random.sample(geneset, mysize))
    return ''.join(genes)

def getfitness(child):
    return sum(1 for a, b in zip(child, target) if a == b)

def mutate(child):
    index = random.randrange(0,len(child))
    newchild = list(child)
    old, new = random.sample(geneset,2)
    if old == newchild[index]:
        newchild[index] = new
    return ''.join(newchild)

def display(child, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = getfitness(child)
    print("{0}\t{1}\t{2}".format(child, fitness, str(timeDiff)))

def getresult():
    random.seed()
    startTime = datetime.datetime.now()
    parent = generateparent(len(target))
    bestFitness = getfitness(parent)
    display(parent, startTime)
    if bestFitness != len(target):
        while True:
            child = mutate(parent)
            childfitness = getfitness(child)
            if bestFitness > childfitness:
                continue
            display(child, startTime)
            if childfitness == len(target):
                break
            bestFitness = childfitness
            parent = child

class benchmark:
    @staticmethod
    def run(function):
        timings =[]
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            start = time.time()
            function()
            sys.stdout = stdout
            seconds = time.time() - start
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i % 10 == 9:
                print("{0} {1:3.2f} {2:3.2f}".format(1 + i, mean, statistics.stdev(timings, mean)))


if __name__ == "__main__":
    benchmark.run(getresult)
