def eveodd():
    num = int(input("Please enter a number: "))

    if (num % 2) == 0 and (num % 4) != 0:
        print("The number",num, "is even and not a multiple of 4")
    elif (num % 4) == 0:
        print("The number",num,"is even and a multiple of 4")
    else:
        print("The number",num, "is not even")

def dive():
    num = int(input("Please enter a number: "))
    check = int(input("Please enter a number to divide by: "))

    if (num % check) == 0:
        print(check,"divides evenly into",num)
    else:
        print(check,"does not divide evenly into",num)

dive()

eveodd()