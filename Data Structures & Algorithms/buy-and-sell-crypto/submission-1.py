class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            maxProfit = max((prices[i] - min), maxProfit)
        return maxProfit