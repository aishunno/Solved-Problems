# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 
# 'A', 'B', and 'C' from string t.

from collections import defaultdict
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        window_start = 0

        minimum_window_substring = {
            "length": sys.maxsize,
            "substring": ""
        }

        char_freq_in_window = defaultdict(int)
        char_freq_in_t = defaultdict(int)

        for char in t: char_freq_in_t[char] += 1

        # Counter for the target string t
        target_condition_count = len(char_freq_in_t)
        window_condition_met_count = 0

        for window_end in range(len(s)):
            if s[window_end] not in char_freq_in_t:
                continue

            char_freq_in_window[s[window_end]] += 1
            
            # check if condition is met
            if char_freq_in_t[s[window_end]] == char_freq_in_window[s[window_end]]:
                window_condition_met_count += 1
            
            while target_condition_count == window_condition_met_count:
                if minimum_window_substring["length"] > (window_end - window_start) + 1:
                    minimum_window_substring["length"] = (window_end - window_start) + 1
                    minimum_window_substring["substring"] = s[window_start:window_end + 1]

                if s[window_start] in char_freq_in_window:
                    char_freq_in_window[s[window_start]] -= 1
                    
                    if char_freq_in_window[s[window_start]] < char_freq_in_t[s[window_start]]:
                        window_condition_met_count -= 1

                window_start += 1
                
        return minimum_window_substring["substring"]



s = Solution()
print(s.minWindow("cabwefgewcwaefgcf", "cae"))