from collections import Counter, defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        frequency_count = defaultdict(int)

        for n in nums:
            frequency_count[n] += 1

        sorted_frequency_count = sorted(
            frequency_count.items(), 
            key=lambda x: x[1], 
            reverse=True)[0: k]
        
        return [tup[0] for tup in sorted_frequency_count]
    

    def topKFrequent2(self, nums, k):
        # Count the frequency of each element
        frequency_count = defaultdict(int)

        for n in nums: frequency_count[n] += 1
        
        # Use a heap to find the top k elements
        return heapq.nlargest(k, frequency_count.keys(), key=frequency_count.get)
    
    def topKFrequent3(self, nums, k):
        # Initialize buckets for storing elements based on their frequency.
        # Each index represents the frequency, and the list at that index contains
        # elements with that frequency. The size is len(nums) + 1 since the maximum
        # frequency of any element can be at most the length of 'nums'.
        frequency_buckets = [[] for _ in range(len(nums) + 1)]

        # Result list to store the top k frequent elements.
        result = []

        # A dictionary to count the frequency of each element in 'nums'.
        # defaultdict(int) initializes a new key with a default value of 0.
        frequency_count = defaultdict(int)

        # Count the frequency of each element in 'nums'.
        for n in nums: frequency_count[n] += 1

        # Populate the frequency_buckets.
        # For each element and its frequency, append the element to the 
        # corresponding bucket indexed by its frequency.
        for element, freq in frequency_count.items():
            frequency_buckets[freq].append(element)

        # Iterate over the frequency_buckets in reverse order (starting from the
        # highest possible frequency). This ensures we encounter the most frequent
        # elements first.
        for freq in range(len(frequency_buckets) - 1, -1, -1):
            # Iterate over each element in the current bucket.
            for element in frequency_buckets[freq]:
                # Add the element to the result list.
                result.append(element)
                # If we have collected k elements, return the result.
                # This check ensures we stop as soon as we have the top k elements,
                # optimizing performance.
                if len(result) == k:
                    return result



s = Solution()
# print(s.topKFrequent([2, 2, 3, 1, 1, 1], 2))
# print(s.topKFrequent2([2, 2, 3, 1, 1, 1], 2))
print(s.topKFrequent3([2, 2, 3, 1, 1, 1], 2))