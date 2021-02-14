#!/usr/bin/env python3
import operator

def tree(plan):
  for xs in plan[1:]:
    plan[0]._data.append(tree(xs))
  return plan[0]

def execute(query):
  for record in query:
    yield record
