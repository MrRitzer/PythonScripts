def solution(l):
    l.sort(key=lambda s: [int(u) for u in s.split('.')])

l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
solution(l)
o = ","
o=o.join(l)
print(o)