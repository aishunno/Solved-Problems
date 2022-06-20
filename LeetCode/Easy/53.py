class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0

            currentSum += n
            maxSub = max(maxSub, currentSum)

        return maxSub

    def maxSubArraySolution2(self, nums):
        maxSum = nums[0]
        currentSum = maxSum

        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(currentSum, maxSum);

        return maxSum;
