#!/usr/bin/env python3
from collections import OrderedDict

people = [
  OrderedDict([('id', '1'), ('name', 'John'), ('age', '30')]),
  OrderedDict([('id', '2'), ('name', 'Michie'), ('age', '25')]),
  OrderedDict([('id', '3'), ('name', 'Little Michie'), ('age', '1')]),
  OrderedDict([('id', '4'), ('name', 'John'), ('age', '3')]),
  OrderedDict([('id', '5'), ('name', 'Morty'), ('age', '1')]),
  OrderedDict([('id', '6'), ('name', 'CoCo'), ('age', '4')])
]

def select(table):
  return {'people': people}[table]
