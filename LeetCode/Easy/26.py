a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

leftPtr = 1
rightPtr = 1

for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        a[leftPtr] = a[i]
        leftPtr += 1
        

print (a, leftPtr)