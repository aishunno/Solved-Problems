from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPtr = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[leftPtr] = nums[i]
                leftPtr += 1
                
        return leftPtr
        