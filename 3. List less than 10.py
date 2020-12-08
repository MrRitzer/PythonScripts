a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
z = []
num = int(input("Please enter a number: "))
for x in a:
    if x < num:
        z.append(x)
print(f'Array = {z}')