class Solution:
    def sortArrayByParity(self, nums):
        nextEvenNumberIndex = 0

        for i in range(0, len(nums)):
            print(nums[i] % 2)
            if nums[i] % 2 == 0:
                nums[nextEvenNumberIndex], nums[i] = nums[i], nums[nextEvenNumberIndex]
                nextEvenNumberIndex += 1
        
        return nums


sl = Solution()
print(sl.sortArrayByParity([1, 23, 12, 3, 4]))