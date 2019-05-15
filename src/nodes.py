import data

class Selection:
  def __init__(self,data,predicate):
    self.data      = data
    self.predicate = predicate
  def next(self):
    row = self.data.next()
    result = []
    while row != 'EOF':
      if row[self.predicate[0]] == self.predicate[2]:
        result.append(row)
      row = self.data.next()
    self.close()
    return result
  def close(self):
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
      self.close()
    else:
      result = 'EOF'
    return result
  def close(self):
    self.index += 1
    return 'EOF'

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
