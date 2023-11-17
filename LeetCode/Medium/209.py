import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart, windowSum = 0, 0
        minSubArrayLength = sys.maxsize

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            
            while windowSum >= target:
                minSubArrayLength = min(minSubArrayLength, (windowEnd - windowStart) + 1)
                windowSum -= nums[windowStart]
                windowStart += 1

        return 0 if minSubArrayLength == sys.maxsize else minSubArrayLength



solution = Solution()
print(solution.minSubArrayLen(7, [2, 1, 5, 2, 3, 2]))