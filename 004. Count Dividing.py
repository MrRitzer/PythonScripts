def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        if n & 1 == 1:
            if n % 4 == 1 or n == 3:
                n = n - 1
            else:
                n = n + 1
        else:
            n = n >> 1
        count = count + 1
    return count
print(solution('15'))