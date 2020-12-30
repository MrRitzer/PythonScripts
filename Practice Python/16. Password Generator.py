import random
import string
def psdrng(strength,length):
    random.seed(random.random())
    psd = []                #Password to be generated
    if strength == 1:
        for x in range(length):
            psd.append(random.choice(string.ascii_lowercase))
    elif strength == 2:
        for x in range(length):
            z = random.randint(1,2)
            if z == 1:
                psd.append(random.choice(string.ascii_lowercase))
            elif z == 2:
                psd.append(random.choice(string.ascii_uppercase))
    elif strength == 3:
        for x in range(length):
            z = random.randint(1,3)
            if z == 1:
                psd.append(random.choice(string.ascii_lowercase))
            elif z == 2:
                psd.append(random.choice(string.ascii_uppercase))
            elif z == 3:
                psd.append(random.choice(string.digits))
    elif strength == 4:
        for x in range(length):
            z = random.randint(1,4)
            if z == 1:
                psd.append(random.choice(string.ascii_lowercase))
            elif z == 2:
                psd.append(random.choice(string.ascii_uppercase))
            elif z == 3:
                psd.append(random.choice(string.digits))
            elif z == 4:
                psd.append(random.choice(string.punctuation))
    psd = "".join(psd)
    return psd