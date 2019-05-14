import util
from collections import OrderedDict

class Selection:
  def __init__(self):
    yield
  def next(self):
    yield
  def close(self):
    return

class Scan:
  def __init__(self):
    self.data = [OrderedDict([('id', '1'), ('name', 'John'), ('age', '30')]), OrderedDict([('id', '2'), ('name', 'Michie'), ('age', '25')])]
    self.iterate_data = util.iterate_data(self)
  def next(self,predicate):
    util.iterate_data(self)
    util.iterate_data(self)
    return self.iterate_data
  def close(self):
    return

class Projection:
  def __init__(self):
    yield
  def next(self):
    yield
  def close(self):
    return

class Sort:
  def __init__(self):
    yield
  def next(self):
    yield
  def close(self):
    return

class Distinct:
  def __init__(self):
    yield
  def next(self):
    yield
  def close(self):
    return
