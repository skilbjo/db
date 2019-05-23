#!/usr/bin/env python3
import util
# from nodes import Projection, Selection, MemScan, Iterator
from nodes import Selection, MemScan, Iterator

# query = util.tree([
  # Projection(lambda r: r.'name'),[
    # Selection(lambda r: r.id == 1),[
      # MemScan(data.people)]]])

query = util.tree([
  Selection(lambda r: r.id == 1),[
    MemScan('people')]])

def execute(plan):
  print('--- query ---')
  print('printing query :',plan)
  result = []
  for record in plan:
    # yield record
    result.append(record)
  return result

def main(function, cmd=None):
  execute(query)
  return

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Run some queries')
  parser.add_argument('-f','--function', help='Function <query|explain>')
  parser.add_argument('-c','--command', help='Text to run <select * from table>')
  args = parser.parse_args()

  main(args.function,args.command)
