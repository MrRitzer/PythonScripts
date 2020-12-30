import random
from random import randint
x = [randint(1,25) for x in range(10)]
print(x)
z = [y for y in x if (y > (z for z in x))]