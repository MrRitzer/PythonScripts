import random
x = int(input("What are your odds? "))
z = (random.randint(1,x))
if z == 1:
    print("Time for a shot!")
else:
    print("No shots yet!")