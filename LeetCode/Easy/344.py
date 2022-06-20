def reverseString(s):
    leftPtr = 0
    rightPtr = len(s) - 1

    while(rightPtr > leftPtr):
        s[leftPtr], s[rightPtr] = s[rightPtr], s[leftPtr]
        leftPtr += 1
        rightPtr -= 1