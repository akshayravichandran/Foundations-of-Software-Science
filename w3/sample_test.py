from sample import Sample
from O import O
import random
import math

def testSample(seed, max):
  # Create a new sample with max size `max`
  s = Sample(max)
  
  # Set seed value to re-produce same random numbers
  random.seed(seed)
  for i in range(1, 10000):
    y = random.uniform(0, 1)
    s.add(y)
  
  print ("50th percentile = ", s.nth(0.5))
  assert 0.4 < s.nth(0.5) < 0.6, "Out of range"

@O.k
def testSampleSize32():
  """Testing Reservoir Sampler with maximum size 32."""
  testSample(1, 32)
  
@O.k
def testSampleSize64():
  """Testing Reservoir Sampler with maximum size 64."""
  testSample(1, 64)
  
@O.k
def testSampleSize128():
  """Testing Reservoir Sampler with maximum size 128."""
  testSample(1, 128)

@O.k
def testSampleSize256():
  """Testing Reservoir Sampler with maximum size 256."""
  testSample(1, 256)

@O.k
def testSampleSize512():
  """Testing Reservoir Sampler with maximum size 512."""
  testSample(1, 512)

@O.k
def testSampleSize1024():
  """Testing Reservoir Sampler with maximum size 1024."""
  testSample(1,1024)
  

if __name__== "__main__":
  O.report()
