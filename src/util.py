def iterate_data(data):
  try:
    for row in iter(data):
      yield row
  except StopIteration:
    return
