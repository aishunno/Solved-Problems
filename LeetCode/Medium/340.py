class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        character_frequency = {}
        windowStart, maxLength = 0, 0

        for windowEnd in range(len(s)):
            right_character = s[windowEnd]

            if right_character not in character_frequency:
                character_frequency[right_character] = 0

            character_frequency[right_character] += 1

            while len(character_frequency) > k:
                left_character = s[windowStart]
                character_frequency[left_character] -= 1

                if character_frequency[left_character] == 0:
                    del character_frequency[left_character]

                windowStart += 1

            maxLength = max(maxLength, (windowEnd - windowStart) + 1)

        return maxLength
    
solution = Solution()
print(solution.lengthOfLongestSubstringKDistinct("eceba", 2))