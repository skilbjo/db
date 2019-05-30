#!/usr/bin/env python3
import data
import util

class PlanNode(object):
  def __init__(self):
    self._data = []
  def __iter__(self):
    return self
  def __next__(self):
    raise NotImplementedError

class NestedLoopJoin(PlanNode):
  def __init__(self):
    super().__init__()
  def __next__(self):
    yield

class Aggregation(PlanNode):
  # def __init__(self, data, type, field): # type enum: sum, count, average
  def __init__(self, type, field): # type enum: sum, count, average
    super().__init__()
    self.type   = type
    self.field  = field
    self.result = {'sum': 0, 'count': 0, 'max': 0, 'min': 0}
  def __next__(self):
    while True:
      record = next(self._data[0])
      self.result['sum']   += record[self.field]
      self.result['count'] += 1
      if self.result['max'] < record[self.field]:
        self.result['max'] = record[self.field]
      if self.result['min'] > record[self.field]:
        self.result['max'] = record[self.field]
    # while loop is a while forever loop; below code will not be run
    print(self.type, self.result['sum'], self.result[self.type])
    if self.type == 'average':
      return self.result['sum'] / self.result['count']
    else:
      return self.result[self.type]

class Selection(PlanNode):
  def __init__(self,predicate):
    super().__init__()
    self.predicate = predicate
  def __next__(self):
    while True:
      record = next(self._data[0])
      if self.predicate(record):
        return record

class Projection(PlanNode):
  def __init__(self,output_fn):
    super().__init__()
    self.output_fn = output_fn
  def __next__(self):
    record = next(self._data[0])
    return tuple(self.output_fn(record))

class MemScan(PlanNode):
  def __init__(self,table):
    super().__init__()
    self.table     = data.select(table)
    self._iterable = iter(self.table)
  def __next__(self):
    return next(self._iterable)

class Sort(PlanNode):
  def __init__(self):
    super().__init__()
  def __next__(self):
    yield

class Distinct(PlanNode):
  def __init__(self):
    super().__init__()
  def __next__(self):
    yield

class Iterator(PlanNode):
  def __init__(self, plan):
    self.plan = plan
  def next(self):
    return util.tree(self.plan)
