import random
a = []
b = []
for x in range(10):
    a.append(random.randint(0,10))
for x in range(10):
    b.append(random.randint(0,10))
d = a + b
z = []
for x in d:
    if x in a and x in b:
        z.append(x)
z = list( dict.fromkeys(z))
print(f'The numbers {z} are in both arrays')