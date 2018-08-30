import re, traceback

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
def testing_failure():
  """This one must fail.. just to
  test if the  unit test system is working"""
  assert 1 == 2

@O.k
def testing_success():
  """If this one fails, we have a problem!"""
  assert 1 == 1
  
@O.k
def testing_page_5():
  """Testing Whitespace Formatting"""
  two_plus_three = 2 + \
                   3
  assert two_plus_three == 5

@O.k
def testing_page_6():
  """Testing Modules"""
  from collections import Counter
  counter = Counter()
  for word in ["apple", "basket", "cat", "apple", "apple", "cat"]:
    counter[word] += 1
  assert counter["apple"] == 3
  assert counter["basket"] == 1
  assert counter["cat"] == 2
  
@O.k
def testing_page_7():
  """Testing Arithmetic"""
  assert 5 // 2 == 2
  
@O.k
def testing_page_8():
  """Testing Functions"""
  def double(x):
    return x * 2
  assert double(4) == 8

@O.k 
def testing_page_9():
  """Testing Strings"""
  single_quoted_string = 'data science'
  double_quoted_string = "data science"
  assert single_quoted_string == double_quoted_string

@O.k
def testing_page_10():
  """Testing Exceptions"""
  try:
    a = 0 / 0
    msg = "No exception thrown"
  except ZeroDivisionError:
    msg = "Exception thrown"
  assert msg == "Exception thrown"

@O.k
def testing_page_11():
  """Testing Lists"""
  list = [1, 2, 3, 4]
  assert sum(list) == 10

@O.k
def testing_page_12():
  """Testing Unpacking of Lists"""
  a, b = [1, 2]
  assert a == 1
  assert b == 2

@O.k
def testing_page_13():
    """Testing Tuples"""
    x, y = (1+5), (2*4)
    assert x == 6
    assert y == 8

@O.k
def testing_page_14():
  """Testing Dictionaries"""
  dict = {"Name": "Akshay", "Group": "F"}
  assert "Name" in dict
  assert dict["Name"] == "Akshay"
  assert dict["Group"] == "F"

@O.k
def testing_page_15():
  """Testing Default Dictionary"""
  from collections import defaultdict
  default_dict = defaultdict(int)
  for word in ["apple", "ball", "cat", "apple", "apple", "apple"]:
    default_dict[word] += 1
  assert default_dict["apple"] == 4
  assert default_dict["ball"] == 1
  assert default_dict["cat"] == 1
  
@O.k
def testing_page_16():
  """Testing Counter"""
  from collections import Counter
  c = Counter([0, 1, 2, 0])
  assert c[0] == 2
  assert c[1] == 1
  assert c[2] == 1

@O.k
def testing_page_17():
  """Testing Sets"""
  s = set()
  s.add("apple")
  s.add("ball")
  s.add("cat")
  assert len(s) == 3
  assert "apple" in s
  assert "ball" in s
  assert "cat" in s

@O.k
def testing_page_18():
  """Testing Control Flow"""
  x = 1
  sum = 0
  while x <= 10:
    sum += x
    x += 1
  assert sum == 55

@O.k
def testing_page_19():
  """Testing Truthiness"""
  one_less_than_two = 1 < 2
  assert one_less_than_two

@O.k
def testing_page_20():
  """Testing Truthiness - all and any"""
  assert all([True, 1 < 2, "string" == 'string'])
  assert any([False, 1 > 2, 5 + 1 == 6])

@O.k
def testing_page_22():
  """Testing Sorting"""
  arr = [4, 2, 6, 1]
  assert sorted(arr) == [1, 2, 4, 6]

@O.k
def testing_page_23():
  """Testing List Comprehensions"""
  even_numbers_till_10 = [x for x in range(11) if x % 2 == 0]
  assert even_numbers_till_10 == [0, 2, 4, 6, 8, 10]
  
@O.k
def testing_page_24():
  """Testing Generators and Iterators"""
  def lazy_range(n):
    i = 1
    while i < n:
      yield i
      i += 2
  sum_of_odd_nums = 0
  for x in lazy_range(10):
    sum_of_odd_nums += x
  assert sum_of_odd_nums == 25
  
@O.k
def testing_page_25():
  """Testing Randomness"""
  import random
  random.seed(10) 
  rand_1 = random.random()
  random.seed(10)
  rand_2 = random.random()
  assert rand_1 == rand_2

@O.k
def testing_page_26():
  """Testing Regular Expressions"""
  assert re.match("a*b+c", "aaaaabbbbbc")

@O.k
def testing_page_27():
  """Testing Object Oriented Programming"""
  class MyList:
    arr = []
    
    def add(self, value):
      self.arr.append(value)
    
    def sum(self):
      s = 0
      for v in self.arr:
        s += v
      return s
    
    def double_all(self):
      return [x*2 for x in self.arr]
  
  my_list = MyList()
  my_list.add(1)
  my_list.add(2)
  my_list.add(6)
  assert my_list.sum() == 9
  assert my_list.double_all() == [2, 4, 12]

@O.k
def testing_page_28():
  """Testing Functional Tools - Partials"""
  from functools import partial
  
  def exp(base, exp):
    return base ** exp
  
  two_to_the = partial(exp, 2)
  
  assert two_to_the(3) == 8

@O.k
def test_page_29():
  """Testing Functional Tools - Reduce"""
  from functools import reduce
  
  def add(a, b):
    return a + b
  
  assert reduce(add, [1, 2, 3, 4]) == 10

@O.k
def test_page_30():
  """Testing Enumerate"""
  words = ["apples", "balls", "cats"]
  map = {}
  for i, word in enumerate(words):
    map[word] = i*2
  assert map["apples"] == 0
  assert map["balls"] == 2
  assert map["cats"] == 4

@O.k
def test_page_31():
  """Testing Zip and Argument Unpacking"""
  a = ['a', 'b', 'c']
  b = [1, 2, 3]
  assert set(zip(a,b)) == {('a', 1), ('b', 2), ('c', 3)}

@O.k
def test_page_32():
  """Testing args"""
  def sum_all(*args):
    sum = 0
    for x in args:
      sum += x
    return sum
  
  assert sum_all(1) == 1
  assert sum_all(1,2) == 3
  assert sum_all(1,2,3,4) == 10
    

@O.k
def test_page_33():
  """Testing kwargs"""
  def get_keys_and_values(**kwargs):
    keys = []
    values = []
    for key, value in kwargs.items():
      keys.append(key)
      values.append(value)
    return keys, values
 
  keys, values = get_keys_and_values(a=1, b=2, c=3, d=4)
  
  assert keys == ['a', 'b', 'c', 'd']
  assert values == [1, 2, 3, 4]

if __name__== "__main__":
  O.report()