import re,traceback

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f

@O.k
def testingFailure():
  """this one must fail.. just to
  test if the  unit test system is working"""
  assert 1==2

@O.k
def testingSuccess():
  """if this one fails, we have a problem!"""
  assert 1==1

DATA1 = """
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""


DATA2 = """
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes
    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,
       
                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

def lines(src):
  """Return contents, one line at a time."""
  if src[-3:] in ["csv", "dat"]:
    file = open(src)
    for line in file:
      yield line
  else:
    for line in src.splitlines():
      yield line

def rows(src):
  """Kill bad characters. If line ends in ',' 
  then join to next. Skip blank lines."""
  cache = ""
  for line in src:
    line = re.sub(r'([ \n\r\t]|#.*)', "", line)
    if line != "":
      cache = cache + line
      if line[-1] != ",":
        line = cache
        cache = ""
        yield line

def cols(src):
  """ If a column name on row1 contains '?', 
  then skip over that column."""
  for row_index, row in enumerate(src):
    cache = list()
    if row_index == 0:
      ignore = list()
      for col_index, col in enumerate(row.split(",")):
        if "?" in col:
          ignore.append(col_index)
        else:
          cache.append(col)
      yield cache
    else:
      for col_index, col in enumerate(row.split(",")):
        if col_index not in ignore:
          cache.append(col)
      yield cache
  
def prep(src):
  """ If a column name on row1 contains '$', 
  coerce strings in that column to a float."""
  for row_index, row in enumerate(src):
    cache = []
    if row_index == 0:
      coerce = []
      for col_index, col in enumerate(row):
        if "$" in col:
          coerce.append(col_index)
        cache.append(col)
      yield cache
    else:
      for col_index, col in enumerate(row):
        if col_index not in coerce:
          cache.append(col)
        else:
          cache.append(float(col))
      yield cache

def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)

@O.k
def ok3(): ok0("sample.csv")

@O.k
def ok4(): ok0("sample.dat")

if __name__== "__main__":
  O.report()