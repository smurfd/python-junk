inf = open("file.txt", 'r') 
i = 0
for line in inf.readlines():
  i += 1
  if len(line) < 81: print("row", i, "has the length", len(line))
