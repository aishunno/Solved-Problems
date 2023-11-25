from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        frequency_count = defaultdict(int)
        frequency_bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for n in nums: frequency_count[n] += 1

        for num, freq in frequency_count.items():
            frequency_bucket[freq].append(num)

        for i in range(len(frequency_bucket) - 1, -1, -1):
            if len(frequency_bucket[i]):
                
                for num in frequency_bucket[i]:
                    if len(result) < k:
                        result.append(num)

        return result
    

s = Solution()
print(s.topKFrequent([2, 2, 3, 1, 1, 1], 2))