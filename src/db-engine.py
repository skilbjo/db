#!/usr/bin/env python3
from collections import OrderedDict

class Selection:
  def __init__(self):
    yield
  def next(self):
    yield
  def close(self):
    return

def while_data(data):
  for row in data:
    try:
      yield row
    except StopIteration:
      return

class Scan:
  def __init__(self):
    self.data = [OrderedDict([('id', '1'), ('name', 'John'), ('age', '30')]), OrderedDict([('id', '2'), ('name', 'Michie'), ('age', '25')])]
  def iterate_data(self):
    while True:
      for row in iter(self.data):
        yield row
  def next(self,predicate):
    row = iterate_data()
    return row
  def close(self):
    return

def execute_plan(plan):
  r = Scan()
  row = next(r.next(True))
  row = next(r.next(True))
  print(row)
  return row

def query():
  return execute_plan('')

def main(function, cmd=None):
  if function == 'query' or function == '':
    return query()

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(description='Run some queries')
  parser.add_argument('-f','--function', help='Function <query|explain>', required=True)
  parser.add_argument('-c','--command', help='Text to run <select * from table>')
  args = parser.parse_args()

  main(args.function,args.command)
