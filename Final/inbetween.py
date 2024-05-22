import math
import mathplotlib.py

t1 = 180
t2 = 300
delta = t2 - t1

for i in range(1, 13):
    tbi = t1 + delta * (1 - math.cos(i * math.pi / 13)) / 2
    print(f"t_{i} = {tbi}")