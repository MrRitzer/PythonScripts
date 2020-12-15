y=["Hello"]
print(y)
y.append("Ritter")
print(y)



def stuff(x):
    if x % 2 == 0:
        print("Num is even")
    else:
        print("Num is odd")
stuff(3)
stuff(4.6)
stuff(1/9)

def stuff2(x):
    n = x & 1
    
    print(n)
stuff2(14)