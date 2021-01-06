def solution(x, y):
    x, y = int(x), int(y)
    gens = 0
    while (x != 1 and y != 1):
        if x % y == 0:
            return "impossible"
        else:
            gens = gens+int(max(x, y)/min(x, y))
            x, y = max(x, y) % min(x, y), min(x, y)
    return str(gens+max(x, y)-1)
print(solution('4','7'))