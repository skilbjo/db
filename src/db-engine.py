#!/usr/bin/env python3
from nodes import Iterator
from nodes import Selection, Scan # for testing

query = {
  'PROJECTION': ['name','id'],
  'SELECTION' : ['id', '>', '2'],
  'FILESCAN'  : ['people']
}

query2 = {
  'AGGREGATION': ['sum','age'],
  'PROJECTION' : ['age'],
  'SELECTION'  : ['id', '>', '2'],
  'FILESCAN'   : ['people']
}

def execute_plan(plan):
  # s = Selection(Scan('people'),['id','=','2']).next()

  s = Iterator(plan)
  s = s.next()

  print('printing s:',s)
  return

def main(function, cmd=None):
  return execute_plan(query2)

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Run some queries')
  parser.add_argument('-f','--function', help='Function <query|explain>')
  parser.add_argument('-c','--command', help='Text to run <select * from table>')
  args = parser.parse_args()

  main(args.function,args.command)
