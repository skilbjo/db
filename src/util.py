def iterate_data(self):
  while True:
    for row in iter(self.data):
      yield row
