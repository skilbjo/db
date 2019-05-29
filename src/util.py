#!/usr/bin/env python3
import operator

# def tree(plan):
  # for xs in plan[1:]:
    # plan[0]._inputs.append(tree(xs))
  # return plan[0]

def tree(nodes):
  for c in nodes[1:]:
    nodes[0]._inputs.append(tree(c))
  return nodes[0]

def execute(query):
  for record in query:
    yield record

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
