from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        longest_sub_string_length = 0
        s = list(s)
        character_frequency = defaultdict(int)

        for window_end in range(len(s)):
            character_frequency[s[window_end]] += 1
            
            max_frequency_key = max(character_frequency, key=character_frequency.get)
            max_frequency_value = character_frequency[max_frequency_key]
            current_window_length = (window_end - window_start) + 1
            
            if (current_window_length - max_frequency_value) <= k:
                longest_sub_string_length = max(
                    longest_sub_string_length,
                    current_window_length
                )
            else:
                character_frequency[s[window_start]] -= 1
                window_start += 1

        return longest_sub_string_length
    
solution = Solution()

print(solution.characterReplacement("AABABBA", 1))