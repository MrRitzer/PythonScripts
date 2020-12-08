import random
a = [random.randint(1,5) for x in range(10)]
b = [x for x in range(10)]
c = [set(a+b)]
print(c)