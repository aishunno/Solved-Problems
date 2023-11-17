class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        used_characters = []
        longest_substring_length = 0

        for window_end in range(len(s)):
            window_last_character = s[window_end]
            used_characters.append(window_last_character)

            while(used_characters.count(window_last_character) > 1):
                window_first_character = s[window_start]
                used_characters.remove(window_first_character)
                window_start += 1

            longest_substring_length = max(
                longest_substring_length, 
                (window_end - window_start) + 1
            )

        return longest_substring_length
    

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))