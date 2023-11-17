from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start, max_length = 0, 0
        fruit_frequency = {}

        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]

            if right_fruit not in fruit_frequency:
                fruit_frequency[right_fruit] = 0
            
            fruit_frequency[right_fruit] += 1

            while len(fruit_frequency) > 2:
                left_fruit = fruits[window_start]

                fruit_frequency[left_fruit] -= 1

                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]

                window_start += 1

            max_length = max(max_length, (window_end - window_start) + 1)
        
        return max_length


solution = Solution()
print(solution.totalFruit([1, 2, 3, 2, 2]))