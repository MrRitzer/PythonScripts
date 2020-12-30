def rvrse(x = []):
    x = str(x)
    tempstr = x.split()
    tempstr = list(reversed(tempstr))
    x = " ".join(tempstr)
    return x
str1 = "This is a string"
str2 = "More string practice!"
print(rvrse(str1))