import random
import math
from w3.sample import Sample

default_max = 512

class Num:
  def __init__(self, max = default_max):
    self.mu = 0
    self.m2 = 0
    self.sd = 0
    self.lo = 10**32
    self.hi = -10**32
    self.sample = Sample(max)
    self.w = 1
    self.n = 0
  
  def bulkAdd(self, values, func = lambda x: x):
    for x in values:
      self.numInc(func(x))
  
  def numInc(self, value):
    if value == '?':
      return
    self.n += 1
    self.sample.add(value)
    d = value - self.mu
    self.mu += d / self.n
    self.m2 += d*(value - self.mu)
    self.hi = value if value > self.hi else self.hi
    self.lo = value if value < self.lo else self.lo
    if self.n >= 2:
      self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5 
  
  def numDec(self, value):
    if value == '?' or self.n == 1:
      return
    self.n -= 1
    d = value - self.mu
    self.mu -= d / self.n
    self.m2 -= d*(value - self.mu)
    if self.n >= 2:
      self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5

  def numNorm(self, value):
    return x == '?' and 0.5 or (x-self.lo) / (self.hi - self.lo + 10**-32)
  
  @staticmethod
  def numXpect(a, b):
    n = a.sample.n + b.sample.n + 0.0001
    return a.sample.n/n * a.sd + b.sample.n/n * b.sd
