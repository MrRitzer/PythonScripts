import random
a = str(random.randint(1,9))
x = 0
z = str("y")
g = 0
gr = 0
while z != "exit":
    while (x != a):
        x = str(input("Guess a number between 1 and 9! "))
        if (x == "exit"):
            z = str("exit")
            x = a
        elif (int(x) > int(a)):
            print("Too high! Guess again!")
            g += 1
        elif (int(x) < int(a)):
            print("Too low! Guess again")
            g += 1
    if (int(x) == int(a) and z != "exit"):
        print("Good job! You guessed right!")
        x = str("0")
        a = str(random.randint(1,9))
        g += 1
        gr += 1
print("You guessed correctly",gr,"times out of",g,"total guesses!")