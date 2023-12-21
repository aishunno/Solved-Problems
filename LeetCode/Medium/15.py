# [-1,0,1,2,-1,-4]
# Two condition 
    # 1. i != j and i != k and j != k 
    # 2. nums[i] + num[j] + num[k] == 0
# Output: [[-1,-1,2],[-1,0,1]]

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array in O(nlogn) time complexity
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            # set target, low and high 
            low, high = i + 1, len(nums) - 1

            while (low < high):
                sum = a + nums[low] + nums[high]

                if sum > 0:
                    high -= 1
                elif sum < 0:
                    low += 1
                else:
                    res.append([a, nums[low], nums[high]])
                    # while low < high and nums[low] == nums[low + 1]:
                    #     low += 1  # Skip duplicates
                    # while low < high and nums[high] == nums[high - 1]:
                    #     high -= 1  # Skip duplicates
                    low += 1
                    high -= 1

        return res


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]));