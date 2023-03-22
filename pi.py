from decimal import *
getcontext().prec = 100000

def pidec(reps):
  result = Decimal(3.0)
  op = 1
  n = 2
  for n in range(2, 2*reps+1, 2):
    result += 4/Decimal(n*(n+1)*(n+2)*op)
    op *= -1
  return result

p = pidec(1000000)

print("Decimal Pi: " + str(p))
 
# using join() + ord() + format()
# Converting String to binary
pb = ''.join(format(ord(i), '08b') for i in str(p))

print("Binary Pi: " + pb)
