class Solution:
    def backspaceCompare(self, s: str, t: str):
        stack_one = []
        stack_two = []
        
        for i in range(0, len(s)):
            if s[i] == "#":
                stack_one.pop()
            else:
                stack_one.append(s[i])

        for i in range(0, len(t)):
            if t[i] == "#":
                stack_two.pop()
            else: 
                stack_two.append(t[i])

        return True if stack_one == stack_two else False
