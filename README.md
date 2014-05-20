time-series
===========

DBA: DynamicTimeWrapping Barycenter Averaging (DBA). 

This is an implementation of the algorithm presented in:
A global averaging method for dynamic time warping, with applications to clustering, Petitjean et. al.
(http://dpt-info.u-strasbg.fr/~fpetitjean/Research/Petitjean2011-PR.pdf)

This AS-IS python script is a translation of Petitjean's Java code of DBA algorithm.

Usage
=====
Suppose you have N time-series data, each with length M.

sequences: a NxM numpy array, each row is a original time-series data
averageSequence: a Nx1 numpy array, for the first time DBA call, this could be a reasonable guess of averageSequence.

DBA(averageSequence, sequences)

Example
=======
# create fake 100x20 time-series data
sequences = np.zeros((100,20))
for i in range(100):
  for j in range(20):
    sequences[i][j] = math.cos(random.random()*j/20.0*math.pi)
            
# generate first guess of averageSeuqnce
averageSequence = np.zeros(20)
choice = (int) (random.random() * 100)
for i in range(20):
  averageSequence[i] = sequences[choice][i]
       
# run DBA several times to get a converged averageSequence
print "[%s]" % " ".join([str(i)for i in averageSequence]) 
    
DBA(averageSequence, sequences)
    
print "[%s]" % " ".join([str(i)for i in averageSequence]) 
    
DBA(averageSequence, sequences)
    
print "[%s]" % " ".join([str(i)for i in averageSequence]) 