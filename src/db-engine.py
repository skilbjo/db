#!/usr/bin/env python3
from nodes import Iterator

query = {
  'PROJECTION': ['name','id'],
  'SELECTION' : ['id', '>', '2'],
  'FILESCAN'  : ['people']
}

query2 = {
  'AGGREGATION': ['sum','age'],
  'PROJECTION' : ['age'],
  'SELECTION'  : ['id', '>=', '0'],
  'FILESCAN'   : ['people']
}

def execute_plan(plan):
  result = Iterator(plan).next()
  return result

def main(function, cmd=None):
  print('--- query ---')
  print('printing query :',query)
  print('printing result:',execute_plan(query))

  print('--- query ---')
  print('printing query :',query2)
  print('printing result:',execute_plan(query2))
  return

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Run some queries')
  parser.add_argument('-f','--function', help='Function <query|explain>')
  parser.add_argument('-c','--command', help='Text to run <select * from table>')
  args = parser.parse_args()

  main(args.function,args.command)
