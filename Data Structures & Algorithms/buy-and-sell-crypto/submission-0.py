class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l -> Buy, r -> Sell
        max_p = 0

        while r < len(prices):
            # Is profitable? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1
        return max_p
        