from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPtr = 0
        totalProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[buyPtr]:
                profit = prices[i] - prices[buyPtr]
                totalProfit += profit
            buyPtr = i
        return totalProfit