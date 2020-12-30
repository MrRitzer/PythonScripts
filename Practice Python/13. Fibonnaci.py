x = int(input("Please enter a number of terms: "))
count = 1
terms = [1,1]
while count+1 != x and x > 2:
    terms.append( (terms[count] + terms[count-1]))
    count += 1
if x < 1:
    print("The sequence can't have less than 1 terms")
elif x == 1:
    terms.pop(1)
    print("The Sequence to",x,"terms is:",terms)
else:
    print("The Sequence to",x,"terms is:",terms)