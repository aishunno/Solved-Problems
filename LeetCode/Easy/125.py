class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        isPalindrome = True

        while (left < right):
            while(not self.isAlphaNumeric(s[left]) and left < right):
                left += 1

            while (not self.isAlphaNumeric(s[right]) and right > left):
                right -= 1
            
            isPalindrome = s[left].lower() == s[right].lower()

            left += 1
            right -= 1

            if not isPalindrome: break;
    
        return isPalindrome


    def isAlphaNumeric(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))


s = Solution()
print(s.isPalindrome(".,"))