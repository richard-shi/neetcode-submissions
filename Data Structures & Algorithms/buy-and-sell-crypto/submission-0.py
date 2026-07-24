class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen, max_profit = prices[0], 0 

        for p in prices[1:]:
            max_profit = max(max_profit, p - lowest_seen)
            lowest_seen = min(lowest_seen, p)

        return max_profit    






    






        