class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxi = 0
        for l in range(0,len(prices)):
            if prices[l]<mini:
                mini = prices[l]
            else:
                profit = prices[l] - mini
                maxi = max(maxi,profit)
        return maxi        


           
       
                 
