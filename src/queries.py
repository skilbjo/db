#!/usr/bin/env python3
from nodes import Aggregation, Projection, Selection, MemScan
from collections import OrderedDict

memscan_numbers = [MemScan('numbers')]
# result: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

memscan_people = [MemScan('people')]
#result: [OrderedDict([('id', '1'), ('name', 'John'), ('age', '30')]), OrderedDict([('id', '2'), ('name', 'Michie'), ('age', '25')]), OrderedDict([('id', '3'), ('name', 'Little Michie'), ('age', '1')]), OrderedDict([('id', '4'), ('name', 'John'), ('age', '3')]), OrderedDict([('id', '5'), ('name', 'Morty'), ('age', '1')]), OrderedDict([('id', '6'), ('name', 'CoCo'), ('age', '4')])]

selection_numbers = [Selection(lambda r: r[0] % 2 == 0),[
                      MemScan('numbers')]]
# result: [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64)]

selection_people = [Selection(lambda r: r['age'] >= 10),[
                     MemScan('people')]]
# result: [OrderedDict([('id', 1), ('name', 'John'), ('age', 30)]), OrderedDict([('id', 2), ('name', 'Michie'), ('age', 25)])]

projection_numbers = [Projection(lambda r: [r[1],r[0]]),[
                       MemScan('numbers')]]
# result: [(0, 0), (1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7), (64, 8), (81, 9)]

projection_people = [Projection(lambda r: [r['name'],r['age']]),[
                      MemScan('people')]]
# result: [('John', 30), ('Michie', 25), ('Little Michie', 1), ('John', 3), ('Morty', 1), ('CoCo', 4)]

projection_people_addition = [Projection(lambda r: [r['name'] + ' fren',r['age'] + 5]),[
                               MemScan('people')]]
# result: [('John fren', 35), ('Michie fren', 30), ('Little Michie fren', 6), ('John fren', 8), ('Morty fren', 6), ('CoCo fren', 9)]

projection_selection_people = [Projection(lambda r: [r['name']]),[
                               Selection(lambda r: r['id'] == 1),[
                                 MemScan('people')]]]
# result: [('John',)]

aggregation_people = [Aggregation('sum',1),
                       [Projection(lambda r: [r['name'], r['age']]),[
                         Selection(lambda r: r['id'] >= 3),[
                           MemScan('people')]]]]
