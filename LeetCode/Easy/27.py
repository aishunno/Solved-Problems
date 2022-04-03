from ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        j = 0

        for i in range(len(nums)):
            if val is nums[i]:
                continue
            else:
                nums[j] = nums[i]
                j = j + 1

        return j
