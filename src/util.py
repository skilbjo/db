import operator

def tree(plan):
  for xs in plan[1:]:
    plan[0]._inputs.append(tree(xs))
  return plan[0]

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
