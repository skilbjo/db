import data

class PlanNode:
  def __init__(self):
    self._inputs = []
  def __iter__(self):
    return next

class Selection(PlanNode):
  def __init__(self,predicate):
    super().__init__()
    self.predicate = predicate
  def __next__(self):
    record = next(self._inputs[0])
    return self.predicate(record)

class MemScan:
  def __init__(self,table):
    super().__init__()
    self.table = data.select(table)
  def __next__(self):
    return next(self._iterable)

class Iterator:
  def __init__(self, plan):
    self.plan = plan
  def next(self):
    return tree(self.plan)
