import re
from w3.num import Num
from w3.sym import Sym

class Data:

  def __init__(self):
    """
    Initialize a Data object.
    """
    self.w = {}
    self.syms = {}
    self.nums = {}
    self.class_col = None
    self.rows = {}
    self.name = {}
    self.use = list()

  def indep(self,c):
    """
    Checks if a column an independent column.
    
    Parameters
    ----------
    c : int
      The column to be checked
    """
    return not self.w[c] and self.class_col != c
  
  def dep(self, c):
    """
    Checks if a column is a dependent column.
    
    Parameters
    ----------
    c : int
      The column to be checked
    """
    return not self.indep(c)
    
  def addRow(self, cells):
    """
    Adds a row of data and re-calculates
    column parameters.

    Parameters
    ----------
    cells : list
      The list of values in the row to be added
    """
    r = len(self.rows)
    self.rows[r] = {}
    # only consider columns that didn't have a ? in header
    for col_index in self.use:
      col_value = cells[col_index]
      if col_value != '?':
        if col_index in self.nums.keys():
          col_value = float(col_value)
          self.nums[col_index].numInc(col_value)
        else:
          self.syms[col_index].symInc(col_value)
      self.rows[r][col_index] = col_value

  def printStatistics(self):
    """
    Outputs the statistics of every numeric and symbolic column.
    """
    print("\n\t               \t\t n\tmode\tfrequency")
    for index, sym in self.syms.items():
      print(index, "\t", self.name[index].ljust(15), "\t", sym.n, "\t", sym.mode, "\t", sym.most)
    
    print("\n\t               \t\t n\t\tmu\t sd")
    for index, num in self.nums.items():
      print(index, "\t", self.name[index].ljust(15), "\t", num.n, "\t", '%10.2f'%(num.mu), "\t", '%.2f'%(num.sd))
    
    
    
def header(header_cells):
  """
  Returns a data object after setting it up using the 
  header.

  Parameters
  ----------
  header_cells : list of strings
    List of all the column names

  Returns
  -------
  Data object
  """
  data = Data()
  for col_index, col_name in enumerate(header_cells):
    if not re.match(r'\?',col_name):
      data.use.append(col_index)
      data.name[col_index] = col_name
      if re.match(r'[<>\$]', col_name):
        data.nums[col_index] = Num()
      else:
        data.syms[col_index] = Sym()
      if re.match(r'<', col_name):
        data.w[col_index] = -1
      elif re.match(r'>', col_name):
        data.w[col_index] = 1
      elif re.match(r'!', col_name):
        data.class_col = col_index
  return data
  
def rows(file_name):
  """
  Returns a Data object built using data from a given
  file.

  Parameters
  ----------
  file_name : file_name
    The name of the file from which data is to be read.

  Returns
  -------
  A Data object
  """
  data = Data()
  with open(file_name, 'r') as file:
    first = True
    line = file.readline()
    while line:
      line = re.sub(r'([ \n\r\t]|#.*)', "", line)
      cells = line.split(',')
      if len(cells) > 0:
        if first:
          first = False
          data = header(cells)
        else:
          data.addRow(cells)
      line = file.readline()
  return data
    
if __name__== "__main__":
  data_1 = rows("w4\\weather.csv")
  data_2 = rows("w4\\weatherLong.csv")
  data_3 = rows("w4\\auto.csv")
  
  print ("\n\n\nweather.csv")
  data_1.printStatistics()
  
  print ("\n\n\nweatherLong.csv")
  data_2.printStatistics()
  
  print ("\n\n\nauto.csv")
  data_3.printStatistics()