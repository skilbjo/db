class Sort:
  def __init__(self):
    return
  def next(self):
    yield

class Distinct:
  def __init__(self):
    return
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

# class Scan:
  # def __init__(self,table):
    # self.table      = data.select(table)
    # self.length     = len(self.table) - 1
    # self.index      = 0
  # def next(self):
    # result = []
    # if self.index < self.length:
      # result = self.table[self.index]
      # self.index += 1
    # elif self.index == self.length:
      # result = self.table[self.index]
      # self.index += 1
    # else:
      # result = 'EOF'
    # return result

# class Iterator:
  # def __init__(self, plan):
    # self.plan = plan
    # self.scan        = node_translation['FILESCAN'](plan['FILESCAN'][0])
    # self.selection   = node_translation['SELECTION'](self.scan, plan['SELECTION'])
    # self.projection  = node_translation['PROJECTION'](self.selection, plan['PROJECTION'])
    # self.aggregation = node_translation['AGGREGATION'](self.projection, plan['AGGREGATION'][0], plan['AGGREGATION'][1]) if 'AGGREGATION' in self.plan else None
    # self.result      = []
  # def next(self):
    # if self.aggregation:
      # row = self.aggregation.next()
      # return row
    # else:
      # row = self.projection.next()
      # while row != 'EOF':
        # self.result.append(row)
        # row = self.projection.next()
      # return [x for x in self.result if x is not None]

# node_translation = {
  # 'AGGREGATION': Aggregation,
  # 'FILESCAN'   : Scan,
  # 'PROJECTION' : Projection,
  # 'SELECTION'  : Selection
# }

# class Projection:
  # def __init__(self, data, fields):
    # from collections import OrderedDict
    # self.data     = data
    # self.fields   = fields # ['id', 'name']
    # self.result   = OrderedDict()
  # def next(self):
    # row = self.data.next()
    # if row == 'EOF' or row is None:
      # return row
    # else:
      # for field in self.fields: # return [row[k] for k in self.fields] # returns list, not OrderedDict
        # self.result.update({field : row[field]})
      # return self.result

# class Aggregation:
  # def __init__(self, data, type, field): # type enum: sum, count, average
    # self.data   = data
    # self.type   = type
    # self.field  = field
    # self.result = {'sum': 0, 'count': 0}
  # def next(self):
    # row = self.data.next()
    # while row != 'EOF':
      # if row is not None:
        # self.result['sum']   += int(row[self.field])
        # self.result['count'] += 1
      # row = self.data.next()
    # if self.type == 'average':
      # return self.result['sum'] / self.result['count']
    # else:
      # return self.result[self.type]
