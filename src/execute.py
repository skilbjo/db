#!/usr/bin/env python3
import util, queries
from nodes import Projection, Selection, MemScan

def execute(plan):
  q = util.tree(plan)
  result = list(util.execute(q))
  print('result:',result)
  return result

def main(function):
  # execute(queries.memscan_query)   # works
  # execute(queries.memscan_people)  # works
  # execute(queries.selection_numbers)  # works
  # execute(queries.selection_people)   # works
  # execute(queries.projection_numbers) # works
  # execute(queries.projection_people)  # works
  # execute(queries.projection_people_addition)  # works
  # execute(queries.projection_selection_people) # works
  execute(queries.aggregation_people) # works
  return

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Run some queries')
  parser.add_argument('-f','--function', help='Function <query|explain>')
  args = parser.parse_args()

  main(args.function)
