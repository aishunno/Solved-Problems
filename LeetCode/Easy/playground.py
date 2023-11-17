def maximumSubArraySumOfSizeK(arr: list, k: int):
    # setting the window start to 0 index
    windowStart, windowSum = 0, 0.0
    maxSubArraySum = float('-inf')

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            avg = windowSum / k
            maxSubArraySum = max(maxSubArraySum, avg)
            windowSum -= arr[windowStart]
            windowStart += 1

    return maxSubArraySum

print(maximumSubArraySumOfSizeK([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))