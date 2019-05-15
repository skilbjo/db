#!/usr/bin/env python3
from nodes import Scan, Selection

query = [
  ["PROJECTION", ["name"]],
  ["SELECTION", ["id", "EQUALS", "5000"]],
  ["FILESCAN", ["movies"]]
]

query2 = [
  ["AVERAGE"],
  ["PROJECTION", ["rating"]],
  ["SELECTION", ["movie_id", "EQUALS", "5000"]],
  ["FILESCAN", ["ratings"]]
]

def execute_plan(plan):
  s = Selection(Scan('names'),['id','=','2']).next()
  print('printing s:',s)
  return s

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
