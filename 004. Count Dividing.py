def solution(n):
    count = 0
    while n > 1:
        if n % 2 != 0:
            count = count + 1
            n = n + 1
        elif n % 2 == 0:
            count = count + 1
            n = n / 2
    print(count)
k = 4
solution(k)
    