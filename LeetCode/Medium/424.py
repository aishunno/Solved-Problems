class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Loop and get a contiguous sub-array window 
        length_of_longest_sub_array = 0
        window_start = 0
        replaceable_character_count = k

        for window_end in range(len(s)):
            if replaceable_character_count == 0:
                break

            window_last_character = s[window_end]

            if window_end != 0 and window_last_character != s[window_end - 1]:
                s[window_end] = s[window_end - 1]
                replaceable_character_count -= 1

            length_of_longest_sub_array = max(
                length_of_longest_sub_array,
                (window_end - window_start) + 1
            )
    
        return length_of_longest_sub_array
    
solution = Solution()

print(solution.characterReplacement("AABABBA", 1))