x = int(input("Please enter a number: "))
for z in range(1,x):
    if (x % int(z)) == 0:
        print(z,"is a divisor of",x)