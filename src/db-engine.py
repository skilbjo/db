#!/usr/bin/env python3
import util
from nodes import Projection, Selection, MemScan

# query = util.tree([
  # Projection(lambda r: r.'name'),[
    # Selection(lambda r: r.id == 1),[
      # MemScan(data.people)]]])

# query = [Selection(lambda r: r.id == 1),[
    # MemScan('people')]]

# query = [Projection(lambda r: r[0]),[
    # MemScan('people')]]

query = [MemScan('people')]

def execute(plan):
  q = util.tree(plan)
  print('--- query ---')
  print('printing    q: ',q)
  print('printing plan: ',plan)
  result = list(util.execute(q))
  print('result:',result)
  return result

def main(function):
  return execute(query)

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Run some queries')
  parser.add_argument('-f','--function', help='Function <query|explain>')
  args = parser.parse_args()

  main(args.function)
