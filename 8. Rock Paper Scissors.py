p1 = 0
p2 = 0
r = str("rock")
p = str("paper")
s = str("scissors")
x = str("z")
while (x != "n"):
    while (p1 < 2 and p2 < 2):
        t1 = str(input("Player 1, rock, paper, or scissors? "))
        t2 = str(input("Player 2, rock, paper, or scissors? "))

        if t1 == r:
            if t2 == s:
                p1 += 1
            else:
                p2 += 1
        elif t1 == p:
            if t2 == r:
                p1 += 1
            else:
                p2 += 1
        elif t1 == s:
            if t2 == p:
                p1 += 1
            else:
                p2 += 1
    if p1 == 2:
        print("Congragulations player 1!")
    else:
        print("Congragulations player 2!")
    x = str(input("Would you like to play again? y/n "))
    if (x == "y"):
        p1 = 0
        p2 = 0