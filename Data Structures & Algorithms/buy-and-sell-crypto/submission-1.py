class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0

        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                profit = max(profit, prices[R] - prices[L])
        
        return profit
