class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            profit=prices[i]-mini
            maxprofit=max(profit,maxprofit)
            mini=min(mini,prices[i])
        return maxprofit    
        