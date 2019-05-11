def generate_plan():
  import os, csv
  dir = os.path.dirname(os.path.realpath(__file__))
  data_dir = dir+'/../data'
  data = []
  with open(data_dir+'/employees.csv','r') as f:
    header = f.readline().replace('\n','').split(',')
    for row in csv.DictReader(f, fieldnames=header):
      data.append(row)
  print(data)
  return
