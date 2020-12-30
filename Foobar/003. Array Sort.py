import random
def solution(psd):
    h = []
    y = 1
    w = 1
    check = 0
    for k in range(-1000,1000):
        for x in range(len(psd)):    
            z = psd[x]
            if z < 0 and z == k:
                check = check + 1
                h.append(psd[x])
            if check == 2:
                for k in range(0,len(h)):
                    w = w * h[k]
                check = 0
                h = []
            if z > 0 and z == k:
                y = y * z
    if x == len(psd) - 1:
        y = y * w
    print(y)
xs = [2, 0, 2, 2, 0]
xy = [-2, -3, 4, -5,-7,-9,-12,13] 
xk = [2,-3,1,0,-5] 
xz = [random.randint(-100,100) for x in range(random.randint(1,25))]
print(xz)
solution(xz)