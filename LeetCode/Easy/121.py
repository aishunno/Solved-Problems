from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buyPtr = 0
        sellPtr = 1

        while sellPtr < len(prices):
            if prices[buyPtr] < prices [sellPtr]:
                profit = prices[sellPtr] - prices[buyPtr]
                maxProfit = max(maxProfit, profit)
            else:
                buyPtr = sellPtr

            sellPtr += 1

            
        return maxProfit