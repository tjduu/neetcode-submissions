class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0
        while r < (len(prices)):
            if prices[r] > prices[l]:
                temp = prices[r] - prices[l]
                maxp = max(maxp,temp)
                r += 1
            else:
                l = r
                r += 1
        return maxp
                
    