import random
import math

default_max = 512

class Sym: 
  def __init__(self):
    self.counts = {}
    self.mode = None
    self.most = 0
    self.n = 0
    self._ent = None
    
  def bulkAdd(self, values, func = lambda x: x):
    for x in values:
      self.symInc(func(x))

  def symInc(self, value):
    if value == '?':
      return
    self._ent = None
    self.n += 1
    self.counts[value] = self.counts.get(value, 0) + 1
    if self.counts[value] > self.most:
      self.mode, self.most = value, self.counts[value]

  def symDec(self, value):
    self._ent = None
    if self.n > 0:
      self.n -= 1
      self.counts[value] -= 1
  
  def symEnt(self):
    if not self._ent:
      self._ent = 0
      for _,n in self.counts.items():
        p = n / self.n
        self._ent -= p*math.log(p,2)
    return self._ent