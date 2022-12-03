import numpy as np
from scipy.ndimage.interpolation import shift

file = open("../inputs/01.txt")
input = file.readlines()

#### TASK 1

increases = -1 # subtract one because the first one will count as increase but shouldn't as per instructions
lastline = 0

for line in input:
  if int(line) > int(lastline):
    increases += 1
  lastline = line

print("Task 1: "+str(increases)+" increases total.")

### TASK 2

increases = -2
last = np.array([0, 0, 0])
lastsum = 0

for line in input:
  if np.sum(last) > lastsum:
    increases += 1
  lastsum = np.sum(last)
  last = shift(last, 1, cval=int(line))

print("Task 2: "+str(increases)+" increases total.")
