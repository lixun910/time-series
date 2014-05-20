"""
DBA
This is an implementation of the algorithm presented in:
A global averaging method for dynamic time warping, with applications to clustering, Petitjean et. al.
(http://dpt-info.u-strasbg.fr/~fpetitjean/Research/Petitjean2011-PR.pdf)

Authors: xunli@asu.edu, william.griffin@asu.edu
"""
import numpy as np
import math, random

########################################################################
class DBA:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, C, sequences):
        """Constructor"""
        self.NIL = -1
        self.DIAGNOAL = 0
        self.LEFT = 1
        self.UP = 2
        # This attribute is used in order to initialize only once the matrixes
        self.MAX_SEQ_LENGTH = 2000;
        # store the cost of the alignment
        self.costMatrix = np.zeros((self.MAX_SEQ_LENGTH, self.MAX_SEQ_LENGTH))
        # store the warping path
        self.pathMatrix = np.ones((self.MAX_SEQ_LENGTH, self.MAX_SEQ_LENGTH))
        # Store the length of the optimal path in each cell
        self.optimalPathLength = np.ones((self.MAX_SEQ_LENGTH, self.MAX_SEQ_LENGTH))
        
        tupleAssociation = [[] for i in range(len(sequences))]
        res = 0.0
        centerLength = len(C)
        
        for T in sequences:
            seqLength = len(T)
            
            self.costMatrix[0][0] = self.distanceTo(C[0], T[0])
            self.pathMatrix[0][0] = self.NIL
            self.optimalPathLength[0][0] = 0;
        
            for i in range(1,centerLength):
                self.costMatrix[i][0] = self.costMatrix[i-1][0] + self.distanceTo(C[i], T[0])
                self.pathMatrix[i][0] = self.UP
                self.optimalPathLength[i][0] = i
                
            for j in range(1, seqLength):
                self.costMatrix[0][j] = self.costMatrix[0][j-1] + self.distanceTo(T[j], C[0])
                self.pathMatrix[0][j] = self.LEFT
                self.optimalPathLength[0][j] = j
                
            for i in range(1, centerLength):
                for j in range(1, seqLength):
                    indiceRes = self.ArgMin3(self.costMatrix[i-1][j-1], self.costMatrix[i][j-1], self.costMatrix[i-1][j])
                    self.pathMatrix[i][j] = indiceRes
                    if indiceRes == self.DIAGNOAL:
                        res = self.costMatrix[i-1][j-1]
                        self.optimalPathLength[i][j] = self.optimalPathLength[i-1][j-1] + 1
                    elif indiceRes == self.LEFT:
                        res = self.costMatrix[i][j-1]
                        self.optimalPathLength[i][j] = self.optimalPathLength[i][j-1] + 1
                    elif indiceRes == self.UP:
                        res = self.costMatrix[i-1][j]
                        self.optimalPathLength[i][j] = self.optimalPathLength[i-1][j] + 1
                    self.costMatrix[i][j] = res + self.distanceTo(C[i], T[j])
                       
            nbTuplesAverageSeq = int(self.optimalPathLength[centerLength-1][seqLength-1] + 1)
             
            i = centerLength -1
            j = seqLength -1
             
            for t in range(nbTuplesAverageSeq-1, -1, -1):
                tupleAssociation[i].append(T[j])
                if self.pathMatrix[i][j] == self.DIAGNOAL:
                    i = i -1
                    j = j -1
                elif self.pathMatrix[i][j] == self.LEFT:
                    j = j - 1
                elif self.pathMatrix[i][j] == self.UP:
                    i = i - 1
                       
            for t in range(0, centerLength):
                C[t] = self.barycenter(tupleAssociation[t])
                                             
    def Min3(self, a, b, c):
        if a < b:
            if a < c:
                return a
            else:
                return c
        else:
            if b < c:
                return b
            else:
                return c
            
    def ArgMin3(self, a, b, c):
        if a < b:
            if a < c:
                return 0
            else:
                return 2
        else:
            if b < c:
                return 1
            else:
                return 2
            
    def distanceTo(self, a, b):
        return (a - b) * (a -b)
    
    def barycenter(self, tab):
        if len(tab) < 1:
            raise "empty double tab"
            
        return sum(tab) / len(tab)
            
if __name__ == "__main__":
    sequences = np.zeros((100,20))
    for i in range(100):
        for j in range(20):
            sequences[i][j] = math.cos(random.random()*j/20.0*math.pi)
            
    averageSequence = np.zeros(20)
    choice = (int) (random.random() * 100)
    for i in range(20):
        averageSequence[i] = sequences[choice][i]
       
    print "[%s]" % " ".join([str(i)for i in averageSequence]) 
    
    DBA(averageSequence, sequences)
    
    print "[%s]" % " ".join([str(i)for i in averageSequence]) 
    
    DBA(averageSequence, sequences)
    
    print "[%s]" % " ".join([str(i)for i in averageSequence]) 
    print
