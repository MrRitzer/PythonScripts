import random
a = [(random.randint(0,100)) for x in range(12)]
z = [x for x in a if x % 2 == 0]
print(z)