from ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(0, len(numbers)):
            required_number = target - numbers[i]
            if visited.get(required_number):
                return [visited[required_number], i + 1]
                break
            visited[numbers[i]] = i + 1
