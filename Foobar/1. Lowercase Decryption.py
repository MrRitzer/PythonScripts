import string
x = input(str("Enter a string: "))
w = []
y = list(string.ascii_lowercase)
z = list(string.ascii_lowercase)
upc = list(string.ascii_uppercase)
z.reverse()
for j in range(len(x)):
    check = 1
    if x[j] == " ":
        w.append(" ")
        check = 0
    for k in range(len(upc)):
        if x[j] == upc[k]:
            w.append(upc[k])
            check = 0
            break
    for k in range(len(y)):
        if x[j] == y[k]:
            w.append(z[k])
            check = 0
            break
    if check == 1:
        w.append(x[j])
o = ""
o=o.join(w)
print(o)