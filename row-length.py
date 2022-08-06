for i, line in enumerate(open("file.txt", 'r').readlines()): if len(line) < 81:
  print("row", i, "has the length", len(line))
