class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        minp = float('inf')
        
        for i in range(len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            elif prices[i] - minp > m:
                m = prices[i] - minp
                
        return m
