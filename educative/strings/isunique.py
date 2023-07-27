def is_unique(input_str):
  ht = {}

  for c in input_str:
    if c in ht:
      return False
    else:
      ht[c] = True

  return True
