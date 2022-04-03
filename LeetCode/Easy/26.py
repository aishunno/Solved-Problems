from typing import List
class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        if not(len(nums)):
            return 0

        leftPtr = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[leftPtr] = nums[i]
                leftPtr += 1
                
        return leftPtr
        
print(Solution.removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4]))