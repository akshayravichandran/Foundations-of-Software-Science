from num import Num
from O import O
import random
import math

@O.k
def testSample():
  """Test Gaussian Sampler"""
  n = Num()
  
  nums = [4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000]
       
  n.bulkAdd(nums)
  
  print("Items seen: ", nums)
  print("mu = ", '%.3f'%(n.mu), "sd = ", '%.3f'%(n.sd))
  assert math.isclose(n.mu, 270.3, rel_tol = 0.01)
  assert math.isclose(n.sd, 231.946, rel_tol = 0.01)

if __name__== "__main__":
  O.report()
