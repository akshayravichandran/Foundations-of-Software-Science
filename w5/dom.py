import random
from w4.w4 import Data
from w4.w4 import rows

# config value
samples = 100

def dom(data, row1, row2):
  """Compares two rows and finds out if row1 dominates row2
     
     Parameters
     ----------
     data : Data
     The data object for which dom scores need to be calculated
     
     row 1: Map
     The first row which is being compared
     
     row 2: The second row which is being compared
  """
  s1, s2, n = 0, 0, 0
  n += len(data.w)
  for c, w in data.w.items():
    a = data.nums[c].numNorm(row1[c])
    b = data.nums[c].numNorm(row2[c])
    s1 = s1 - 10 ** (w * (a - b) / n)
    s2 = s2 - 10 ** (w * (b - a) / n)
  return s1 / n < s2 / n

def doms(data):
  """Calculates the dom scores for all the rows in the given
     data object
     
     Parameters
     ----------
     data : Data
     The data object for which dom scores need to be calculated
  """
  n = samples
  c = len(data.name)
  for _, row1 in data.rows.items():
    row1[c] = 0
    for s in range(n):
      row2 = random.choice(list(data.rows.values()))
      if row1 == row2:
        continue
      else:
        s = dom(data, row1, row2) and 1/n or 0
        row1[c] += s
  
def printDomScores(data):
  """Helper method to print all dom scores for the given data object
      
     Parameters
     ----------
     data : Data
     The data object for which dom scores need to be printed
  """
  domIndex = len(data.name)
  for _, value in data.name.items():
    print(value, " ", end = "")
  print("dom")
  
  sortedRows = sortByDomScore(list(data.rows.values()), domIndex)
  
  for row in sortedRows:
    for i, value in row.items():
      if i == domIndex: 
        print('%.2f'%(value), " ", end = "")
      else:
        print(value, " ", end = "")
    print("")

def printBestAndWorstDomScores(data, n=5):
  """Helper method to print the top n and bottom n dom scores
  of the given data object
  
  Parameters
     ----------
     data : Data
     The data object for which dom scores need to be printed
     
     n : int
     The number of rows at the top and bottom that need to be printed
  """
  domIndex = len(data.name)
  for _, value in data.name.items():
    print(value, " ", end = "")
  print("dom")
  
  sortedRows = sortByDomScore(list(data.rows.values()), domIndex)
  
  for row in sortedRows[:n]:
    for i, value in row.items():
      if i == domIndex: 
        print('%.2f'%(value), " ", end = "")
      else:
        print(value, " ", end = "")
    print("")
  print(".......")
  for row in sortedRows[-n:]:
    for i, value in row.items():
      if i == domIndex: 
        print('%.2f'%(value), " ", end = "")
      else:
        print(value, " ", end = "")
    print("")
  
    
def sortByDomScore(rows, domIndex):
  """
    Helper method to sort the rows in decreasing order of their dom scores
    
    Parameters
    ----------
    rows : list of maps
    The list of rows to be sorted
    
    domIndex : int
    The key of the dom score entry in the row
  """
  return sorted(rows, key=lambda r: -r[domIndex])
  

if __name__== "__main__":
  data1 = rows("w5\\weatherLong.csv")
  doms(data1)
  print("\nweatherLong.csv")
  printDomScores(data1)
  data2 = rows("w5\\auto.csv")
  doms(data2)
  print("\nauto.csv")
  printBestAndWorstDomScores(data2)