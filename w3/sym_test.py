from sym import Sym
from O import O
import random
import math

@O.k
def testSample():
  """Testing Entropy Sampler"""
  s = Sym()
  syms = ['y','y','y','y','y','y','y','y','y',
	        'n','n','n','n','n']
  s.bulkAdd(syms)
  print("Items = ", syms)
  print("Entropy = ", '%.4f'%(s.symEnt()))
  assert math.isclose(s.symEnt(), 0.9403, rel_tol = 0.01)
  
if __name__== "__main__":
  O.report()
