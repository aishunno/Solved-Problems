def averageOfSubArrayOfSizeK(arr: list[int], k: int) -> list[int]:
    # [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = []
    windowStart, windowSum = 0, 0

    for  windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        if windowEnd >= k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result

print(averageOfSubArrayOfSizeK([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))