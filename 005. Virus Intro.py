import random
def solution(x,y):
    arrF = [int(x),int(y)]
    M = 1
    F = 1
    gens1 = -1
    gens2 = 0
    arrI = [M,F]
    while arrI != arrF:
        arrI = [M,F]
        x = random.randint(1,2)
        if x == 1:
            M = M + F
            F = F
            gens1 = gens1 + 1
        if x == 2:
            M = M
            F = F + M
            gens1 = gens1 + 1
        if M > 10^50 or F > 10^50:
            gens1=-1
            M = 1
            F = 1
            gens2 = gens2 + 1
        if gens2 > 10^50:
            gens1 = 'impossible'
            break

    return str(gens1)
print(solution ('0','1'))