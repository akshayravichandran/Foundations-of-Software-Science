import random
import math

default_max = 512

class Sample:
  def __init__(self, max = default_max, txt=""):
    self.max = max
    self.txt = txt
    self.rank = 1
    self.n = 0
    self.isSorted = False
    self.some = []

  def add(self, value):
    self.n = self.n + 1
    length = len(self.some)
    if length < self.max:
      self.isSorted = False
      self.some.append(value)
    elif random.uniform(0, 1) < length / self.n:
      self.isSorted = False
      self.some[math.floor(random.uniform(0, 1)*length)] = value
    return value
  
  def sampleSorted(self):
    if not self.isSorted:
      self.some.sort()
      self.isSorted = True
    
  def nth(self, n):
    self.sampleSorted()
    return self.some[min(len(self.some), max(1, math.floor(0.5 + len(self.some)*n)))]
  
  def nths(self, ns = [0.1,0.3,0.5,0.7,0.9]):
    out = []
    for n in ns:
      out.append(self.nth(n))
    return out
  
  def sampleLt(self, l2):
    return self.nth(0.5) < l2.nth(0.5)
    
      