from typing import List


class Solution:
    # Brute force 
    def longestConsecutive1(self, nums: List[int]) -> int:
        if not nums: return 0

        longest_streak = 1

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
    # Sorting 
    def longestConsecutive2(self, nums: List[int]) -> int: 
        if not nums: return 0
        
        current_streak = 1
        longest_streak = 1

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1: 
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
    
    # Using hash-set 
    def longestConsecutive3(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

s = Solution()
# print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive3([3]))