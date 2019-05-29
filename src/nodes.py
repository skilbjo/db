#!/usr/bin/env python3
import data
import util

class PlanNode(object):
  def __init__(self):
    self._inputs = []
  def __iter__(self):
    return self
  def __next__(self):
    raise NotImplementedError

class Projection(PlanNode):
  def __init__(self,mapping):
    super().__init__()
    self.mapping = mapping
  def __next__(self):
    record = next(self._inputs[0])
    return tuple(self.mapping(record))

class MemScan(PlanNode):
  def __init__(self,table):
    super().__init__()
    self.table     = data.select(table)
    self._iterable = iter(self.table)
  def __next__(self):
    return next(self._iterable)

class Selection(PlanNode):
  def __init__(self,predicate):
    super().__init__()
    self.predicate = predicate
  def __next__(self):
    while True:
      record = next(self._inputs[0])
      if self.predicate(record):
        return record

class Iterator(PlanNode):
  def __init__(self, plan):
    self.plan = plan
  def next(self):
    return util.tree(self.plan)
