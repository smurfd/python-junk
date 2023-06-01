# Stresstesting
import multiprocessing
import math
 
# CPU usage
def task_cpu(arg): sum([math.sqrt(i) for i in range(1, arg)])

# Disk usage
def task_io(arg):
  data="0"
  for d in range(1, 1000000):
    data = data + str(d)

  for _ in range(arg):
    f = open('workfile', "r+")
    f.read()
    f.seek(0)
    f.write(data)
    f.truncate()

# Network usage
def task_net(arg):
  print("net")

if __name__ == '__main__':
  with multiprocessing.Pool(8) as pool:
    pool.map(task_cpu, range(1,50000))
    pool.map(task_io, range(1,5))
  print('OK')
