def prime(x):
    if x <= 1:
        print("Number is not valid")
        exit(0)
    for z in range(1,x):
        if x % z == 0 and z >= 2:
            t = 1
            break
        else:
            t = 0
    if t == 1:
        print("The number",x,"is not a prime number")
    elif t == 0: 
        print("The number",x,"is a prime number!")

prime(x = int(input("Please enter a number ")))