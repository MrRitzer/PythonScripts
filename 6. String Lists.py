word = str(input("Please enter a string: "))
z = []

for x in reversed(range(len(word))):
    z.append(word[x])
if z == list(word):
    print("The word",word,"is a palindrome")
else:
    print("The word",word,"is not a palindrome")