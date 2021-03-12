import numpy as np
from utils import *
import matplotlib.pyplot as plt
import itertools
import time

# PROJECT EULER 90
def euler90():
    sqs = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)]
    ns = [0,1,2,3,4,5,6,7,8,6]
    combs = list(itertools.combinations(ns,6))
    count = 0
    for i,c1 in enumerate(combs):
        for c2 in combs[:i]:
            fl = np.ones(len(sqs))
            for n,sq in enumerate(sqs):
                if (sq[0] in c1 and sq[1] in c2) or (sq[1] in c1 and sq[0] in c2):
                    fl[n] = 0
            if fl.sum() == 0:
                count+=1

    return count
                

print(euler90())



    
