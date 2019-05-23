import operator

operator = {
    '=' : operator.eq,
    '!=': operator.ne,
    '>' : operator.gt,
    '>=': operator.ge,
    '<' : operator.lt,
    '<=': operator.le
}

def iterate_data(data):
  try:
    for row in iter(data):
      yield row
  except StopIteration:
    return
