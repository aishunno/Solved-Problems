class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        characterFrequencyOfFirstString = dict()
        characterFrequencyOfSecondString = dict()

        for i in range(len(s)):
            characterFrequencyOfFirstString[s[i]] = characterFrequencyOfFirstString.get(s[i], 0) + 1

            characterFrequencyOfSecondString[t[i]] = characterFrequencyOfSecondString.get(t[i], 0) + 1

        return characterFrequencyOfFirstString == characterFrequencyOfSecondString
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))