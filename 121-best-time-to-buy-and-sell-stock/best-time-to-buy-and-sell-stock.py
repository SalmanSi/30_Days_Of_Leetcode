class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # max_=0
        # maxlist=[0]*len(prices)
        # for i in range(len(prices)-1,-1,-1):
        #     max_=max(max_,prices[i])
        #     maxlist[i]=max_
        # ans=0
        # for i in range(len(prices)):
        #     ans=max(ans,-prices[i]+maxlist[i])
        # return ans

        profit=0
        buyprice=prices[0]
        for num in prices[1:]:
            if num<buyprice:
                buyprice=num
            profit=max(profit,num-buyprice)
        return profit

