from collections import OrderedDict

class Selection:
  def __init__(self,data,predicate):
    self.data      = data
    self.predicate = predicate
  def next(self):
    row = self.data.next()
    row = self.data.next()
    row = self.data.next()
    print(row)
    result = []
    # while row != 'EOF':
      # if row[self.predicate[0]] == self.predicate[2]:
        # print(row[self.predicate[0]] == self.predicate[2])
        # result.append(row)
      # row = self.data.next()
    # self.close()
    return result
  def close(self):
    return 'EOF'

class Scan:
  def __init__(self):
    self.data       = [OrderedDict([('id', '1'), ('name', 'John'), ('age', '30')]), OrderedDict([('id', '2'), ('name', 'Michie'), ('age', '25')])]
    self.length     = len(self.data) - 1
    self.index      = 0
    # self.child_data = util.iterate_data(self.data)
  def next(self):
    result = []
    if self.index < self.length:
      result = self.data[self.index]
      self.index += 1
    elif self.index == self.length:
      result = self.data[self.index]
      self.close()
    else:
      result = 'EOF'
    print(result)
    return result
  def close(self):
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
