import numpy as np
distance = [10,23,24,56]
time = [12,23,24,25]

dist = np.array(distance)
t = np.array(time)

vel = dist/t
print(vel)
