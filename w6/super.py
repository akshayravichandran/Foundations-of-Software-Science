from w3.num import Num
from w4.w4 import rows
from w4.w4 import Data
from w5.dom import doms
import sys
import math

class Super:

  def __init__(self, data):
    self.rows = data.rows.values()
    self.goal = len(data.name)
    self.enough = len(self.rows) ** 0.5  # magic constant
  
  def band(self, c, lo, hi):
    if lo == 0:
      return '..' + str(self.rows[hi][c])
    elif hi == most:
      return str(self.rows[lo][c]) + '..'
    else:
      return str(self.rows[lo][c]) + '..' + str(self.rows[hi][c])
  
  def argmin(self, c, lo, hi):
    cut = False
    xl, xr = Num(), Num()
    yl, yr = Num(), Num()
    for i in range(lo, hi+1):
      xr.numInc(self.rows[i][c])
      yr.numInc(self.rows[i][self.goal])
    bestx = xr.sd
    besty = yr.sd
    mu = yr.mu
    if hi - lo > 2*self.enough:
      for i in range(lo, hi+1):
        x = self.rows[i][c]
        y = self.rows[i][self.goal]
        xl.numInc(x)
        xr.numDec(x)
        yl.numInc(y)
        yr.numDec(y)
        if xl.n >= self.enough and xr.n >= self.enough:
          tmpx = Num.numXpect(xl,xr) * 1.05 # magic constant
          tmpy = Num.numXpect(yl,yr) * 1.05
          # print('i=',i,' c=',c,' tmpx=',tmpx,' bestx',bestx)
          if tmpx < bestx:
            if tmpy < besty:
              cut, bestx, besty = i, tmpx, tmpy
    return cut, mu
  
  def cuts(self, c, lo, hi, pre):
    txt = pre + str(self.rows[lo][c]) + '..' + str(self.rows[hi][c])
    cut, mu = self.argmin(c, lo, hi)
    if cut:
      print(txt)
      self.cuts(c, lo, cut, pre + '|..')
      self.cuts(c, cut+1, hi, pre + '|..')
    else:
      b = self.band(c, lo, hi)
      print(txt + ' ==> ', '%.2f'%(math.floor(100*mu)))
      for r in range (lo, hi+1):
        self.rows[r][c] = b

def stop(c, t):
  for i in range(len(t)-1, -1, -1):
    if t[i][c] != '?':
      return i
  return 0

if __name__== "__main__":
  data = rows(sys.argv[1])
  doms(data)
  s = Super(data)
  for c in data.use:
    if data.indep(c) and c in data.nums:
      s.rows = sorted(s.rows, key=lambda r: r[c] if r[c] != '?' else sys.maxsize)
      most = stop(c, s.rows)
      print('\n-- ', data.name[c], most, '----------')
      s.cuts(c, 0, most, "|.. ")
  for _, name in data.name.items():
    print(name.replace('$','') + '\t', end = '')
  print()
  for row in s.rows:
    for i, v in enumerate(row.values()):
        if i == len(data.name):
          print('%.2f'%(v), end = "\t")
        else:
          print(v, end = "\t")
    print()