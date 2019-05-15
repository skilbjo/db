#!/usr/bin/env python3
from collections import OrderedDict

names = [OrderedDict([('id', '1'), ('name', 'John'), ('age', '30')]), OrderedDict([('id', '2'), ('name', 'Michie'), ('age', '25')])]

def select(table):
  return {'names': names}[table]
