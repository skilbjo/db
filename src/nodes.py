import data, operator

operator = {
    "=" : operator.eq,
    "!=": operator.ne,
    ">" : operator.gt,
    ">=": operator.ge,
    "<" : operator.lt,
    "<=": operator.le
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
    self.fields   = fields # ["id", "name"]
  def next(self):
    dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    row = self.data.next()
    result = dictfilt(row, fields)
    return result

class Aggregation:
  def __init__(self,type): # type enum: sum, count, average
    yield
  def next(self):
    yield

class Sort:
  def __init__(self):
    yield
  def next(self):
    yield

class Distinct:
  def __init__(self):
    yield
  def next(self):
    yield

node_translation = {
  "AGGREGATION": Aggregation,
  "FILESCAN"   : Scan,
  "PROJECTION" : Projection,
  "SELECTION"  : Selection
}

class Iterator:
  def __init__(self, plan):
    self.plan = plan
    self.scan       = node_translation["FILESCAN"](plan["FILESCAN"][0])
    self.selection  = node_translation["SELECTION"](self.scan, plan["SELECTION"])
    self.projection = node_translation["PROJECTION"](self.selection, plan["PROJECTION"][0])
    self.result     = []
  def next(self):
    row = self.selection.next()
    while row != 'EOF':
      self.result.append(row)
      row = self.selection.next()
    return [x for x in self.result if x is not None]
