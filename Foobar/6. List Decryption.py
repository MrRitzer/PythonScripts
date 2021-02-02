import random
def solution(l):
    count = 0
    for lk in [x for x in reversed(range(len(l))) if x > 1]:
        for lj in [x for x in reversed(range(len(l))) if x > 0]:
                for li in reversed(range(len(l)-2)):
                    temp = [l[li],l[lj],l[lk]]
                    if (temp[0]<temp[1]<temp[2]):
                        if (temp[2] % temp[1] == 0 and temp[1] % temp[0] == 0):
                            count = count + 1
                    if (temp[0]==temp[1]==temp[2]):
                        if (li == lj or li == lk or lj == lk):
                            break
                        count = count + 1
    return count
                        

l1 = [1, 2, 3, 4, 5, 6,7,8,9]
l2 = [1, 1, 2]
l3 = [1,1]
l4 = [1,3,999999]
l5 = [random]

print(solution(l4))