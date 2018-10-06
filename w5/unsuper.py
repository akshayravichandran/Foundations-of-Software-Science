from w3.num import Num
from w4.w4 import rows
from w4.w4 import Data

class Unsuper:

  def __init__(self, data):
    """
    Initialize an unsupervised learner.
    """
    self.rows = data.rows.values()
    self.enough = len(self.rows) ** 0.5  # magic constant
    print('Enough', self.enough)
  
  def band(self, c, lo, hi):
    if lo == 0:
      return '..' + str(self.rows[hi][c])
    elif hi == most:
      return str(self.rows[lo][c]) + '..'
    else:
      return str(self.rows[lo][c]) + '..' + str(self.rows[hi][c])
  
  def argmin(self, c, lo, hi):
    cut = False
    if hi - lo > 2*self.enough:
      l, r = Num(), Num()
      for i in range(lo, hi+1):
        r.numInc(self.rows[i][c])
      best = r.sd
      for i in range(lo, hi+1):
        x = self.rows[i][c]
        l.numInc(x)
        r.numDec(x)
        if l.n >= self.enough and r.n >= self.enough:
          tmp = Num.numXpect(l,r) * 1.05 # magic constant
          if tmp < best:
            cut, best = i, tmp
    return cut
  
  def cuts(self, c, lo, hi, pre):
    txt = pre + str(self.rows[lo][c]) + '..' + str(self.rows[hi][c])
    cut = self.argmin(c, lo, hi)
    if cut:
      print(txt)
      self.cuts(c, lo, cut, pre + '|..')
      self.cuts(c, cut+1, hi, pre + '|..')
    else:
      b = self.band(c, lo, hi)
      print(txt + ' (' + b + ') ')
      for r in range (lo, hi+1):
        self.rows[r][c] = b
  
def stop(c, t):
  for i in range(len(t)-1, -1, -1):
    if t[i][c] != '?':
      return i
  return 0

if __name__== "__main__":
  data = rows("w5\\weatherLong.csv")
  u = Unsuper(data)
  for c in data.use:
    if data.indep(c) and c in data.nums:
      u.rows = sorted(u.rows, key=lambda r: r[c])
      most = stop(c, u.rows)
      print('\n-- ', data.name[c], most, '----------')
      u.cuts(c, 0, most, "|.. ")
  for _, name in data.name.items():
    print(name.replace('$','') + '\t', end = '')
  print()
  for row in u.rows:
    for i, v in enumerate(row.values()):
      if i == 1:
        print(v.ljust(10), end = "\t")
      else:
        print(v, end = "\t")
    print()