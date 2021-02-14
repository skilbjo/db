#!/usr/bin/env python3
import datetime
from collections import OrderedDict

people = [OrderedDict([('id', 1), ('name', 'John'),          ('age', 30)]),
          OrderedDict([('id', 2), ('name', 'Michie'),        ('age', 25)]),
          OrderedDict([('id', 3), ('name', 'Little Michie'), ('age', 1)]),
          OrderedDict([('id', 4), ('name', 'John'),          ('age', 3)]),
          OrderedDict([('id', 5), ('name', 'Morty'),         ('age', 1)]),
          OrderedDict([('id', 6), ('name', 'CoCo'),          ('age', 4)])]

orders = [OrderedDict([('id', 1), ('person_id', 1), ('name', 'Burger King'),     ('ordered_date', datetime.date(2019,1,1))]),
          OrderedDict([('id', 2), ('person_id', 2), ('name', 'McDonald\'s'),     ('ordered_date', datetime.date(2019,3,1))]),
          OrderedDict([('id', 3), ('person_id', 3), ('name', 'In-N-Out'),        ('ordered_date', datetime.date(2019,2,1))]),
          OrderedDict([('id', 4), ('person_id', 4), ('name', 'Jack in the Box'), ('ordered_date', datetime.date(2019,6,1))]),
          OrderedDict([('id', 5), ('person_id', 5), ('name', 'Taco Bell'),       ('ordered_date', datetime.date(2019,5,1))]),
          OrderedDict([('id', 6), ('person_id', 6), ('name', 'Carl\'s Jr.'),     ('ordered_date', datetime.date(2019,1,1))]),
          OrderedDict([('id', 6), ('person_id', 6), ('name', 'Chick-Fil-A'),     ('ordered_date', datetime.date(2019,2,1))])]

numbers = [(n, n*n) for n in range(10)]

def select(table):
  return {'people' : people,
          'orders' : orders,
          'numbers': numbers}[table]
