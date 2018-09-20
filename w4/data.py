import re
from w3.num import Num
from w3.sym import Sym

class Data:

  def __init__(self):
    """
    Initialize a Data object.
    """
    this.w = {}
    this.syms = {}
    this.nums = {}
    this.class_col = nil
    this.rows = {}
    this.name = {}
    this.use = {}

  def indep(self,c):
    """
    Checks if a column an independent column.
    
    Parameters
    ----------
    c : int
      The column to be checked
    """
    return not this.w[c] and this.class_col != c
  
  def dep(self, c):
    """
    Checks if a column is a dependent column.
    
    Parameters
    ----------
    c : int
      The column to be checked
    """
    return not this.indep(c)
    
  def addRow(self, cells):
    """
    Adds a row of data and re-calculates
    column parameters.

    Parameters
    ----------
    cells : list
      The list of values in the row to be added
    """
    r = self.rows.len
    self.rows[r] = {}
    for use_index, col_index in self.use.items():
      col_value = cells[col_index]
      if col_value != '?':
        if self.nums[use_index]:
          col_value = float(col_value)
          self.nums[use_index].numInc(col_value)
        else:
          self.syms[use_index].symInc(col_value)
      self.rows[r][use_index] = col_value

  def printStatistics(self):
    """
    Outputs the statistics of every numeric and symbolic column.
    """
    print ("\n \t \t n \t mode \t frequency")
    for index, sym in self.syms.items():
      print(index, "\t ", self.name[index], "\t ", sym.n, "\t ", sym.mode, "\t ", sym.most)
    
    print("\n \t \t n \t mu \t sd")
    for index, num in self.nums.items():
      print(index, "\t ", self.name[index], "\t ", num.n, "\t ", num.mu, "\t ", num.sd)
    
    
    
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
  for col_index, col_name in header_cells.items():
    if not re.match(r'\?',col_name):
      c = data.use.len
      data.use[c] = col_index
      data.name[c] = col_name
      if re.match(r'[<>\$]', col_name):
        data.nums[c] = Num()
      else:
        data.syms[c] = Sym()
      if re.match(r'<', col_name):
        data.w[c] = -1
      elif re.match(r'>', col_name):
        data.w[c] = 1
      elif re.match(r'!', col_name):
        data.class_col = c
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
    line = file.readline
    while line:
      line = re.sub(r'([ \n\r\t]|#.*)', "", line)
      cells = line.split(',')
      if cells.len > 0:
        if first:
          first = False
          data = header(cells)
        else:
          data.addRow(cells)
      line = file.readline
  return data
    
  
  