import data, operator
from collections import OrderedDict

operator = {
    '=' : operator.eq,
    '!=': operator.ne,
    '>' : operator.gt,
    '>=': operator.ge,
    '<' : operator.lt,
    '<=': operator.le
}

class Selection:
  def __init__(self,data,predicate):
    self.data      = data
    self.predicate = predicate
  def next(self):
    row = self.data.next()
    if row != 'EOF':
      if operator[self.predicate[1]](row[self.predicate[0]], self.predicate[2]):
        return row
    else:
      return 'EOF'

class Scan:
  def __init__(self,table):
    self.table      = data.select(table)
    self.length     = len(self.table) - 1
    self.index      = 0
  def next(self):
    result = []
    if self.index < self.length:
      result = self.table[self.index]
      self.index += 1
    elif self.index == self.length:
      result = self.table[self.index]
      self.index += 1
    else:
      result = 'EOF'
    return result

class Projection:
  def __init__(self, data, fields):
    self.data     = data
    self.fields   = fields # ['id', 'name']
  def next(self):
    row = self.data.next()
    result = OrderedDict()
    if row == 'EOF' or row is None:
      return row
    else:
      for field in self.fields: # return [row[k] for k in self.fields] # returns list, not OrderedDict
        result.update({field : row[field]})
      return result

class Aggregation:
  def __init__(self, data, type, field): # type enum: sum, count, average
    self.type   = type
    self.field  = field
    self.result = {'sum': 0, 'count': 0}
  def next(self):
    row = self.data.next()
    while row != 'EOF' and row is not None:
      self.result['sum']   += row[field]
      self.result['count'] += 1
      row = self.data.next()
    if self.type == 'average':
      return self.result['sum'] / self.result['count']
    else:
      return self.result[self.type]

class Sort:
  def __init__(self):
  def next(self):
    yield

class Distinct:
  def __init__(self):
  def next(self):
    yield

class NestedLoopJoin:
  def __init__(self, r, s, r_key, s_key):
    self.r = r
    self.s = s
    self.r_key = r_key
    self.s_key = s_key
  def next(self):
    yield

node_translation = {
  'AGGREGATION': Aggregation,
  'FILESCAN'   : Scan,
  'PROJECTION' : Projection,
  'SELECTION'  : Selection
}

class Iterator:
  def __init__(self, plan):
    self.plan = plan
    self.scan        = node_translation['FILESCAN'](plan['FILESCAN'][0])
    self.selection   = node_translation['SELECTION'](self.scan, plan['SELECTION'])
    self.projection  = node_translation['PROJECTION'](self.selection, plan['PROJECTION'])
    self.aggregation = node_translation['AGGREGATION'](plan['AGGREGATION'][0], plan['AGGREGATION'][1])
    self.result      = []
  def next(self):
    if 'AGGREGATION' not in self.plan.keys():
      row = self.aggregation.next()
      while row != 'EOF':
        self.result.append(row)
        row = self.projection.next()
      return [x for x in self.result if x is not None]
    else:
      row = self.projection.next()
      while row != 'EOF':
        self.result.append(row)
        row = self.projection.next()
      return [x for x in self.result if x is not None]
