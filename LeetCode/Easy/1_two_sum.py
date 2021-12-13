from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            req_num = target - n
            if req_num in visited:
                return [visited[req_num], i]
            else:
                visited[n] = i
        