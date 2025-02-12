class Solution:

    def digSum(self,num):
        sum=0
        while num>0:
            sum+=num%10
            num=num//10
        return sum

    def maximumSum(self, nums: List[int]) -> int:
        digSum_nums={}
        for i in range(len(nums)):
            key=self.digSum(nums[i])
            if key not in digSum_nums:
                digSum_nums[key]=[-nums[i]]
            else:
                heapq.heappush(digSum_nums[key],-nums[i])
        ans=-1
        for key,value in digSum_nums.items():
            if len(value)>1:
                ans=max(ans,(-heapq.heappop(value)-heapq.heappop(value))) 
        return ans
                