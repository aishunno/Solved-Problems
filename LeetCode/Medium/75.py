from ast import List


class Solution:
    def array_partition(self, nums, start, end):
        pivot = nums[end]
        pIndex = start

        for i in range(start, end):
            if nums[i] <= pivot:
                nums[pIndex], nums[i] = nums[i], nums[pIndex]
                pIndex += 1

        nums[pIndex], nums[end] = nums[end], nums[pIndex]
        return pIndex

    def quick_sort(self, nums, start, end):
        if start < end:
            pIndex = self.array_partition(nums, start, end)
            self.quick_sort(nums, start, pIndex - 1)
            self.quick_sort(nums, pIndex + 1, end)

    def sortColors(self, nums: List[int]) -> None:
        self.quick_sort(nums, 0, len(nums) - 1)
