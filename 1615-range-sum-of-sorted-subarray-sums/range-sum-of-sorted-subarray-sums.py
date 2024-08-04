class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums=[]
        for i in range(n):
            sums.append(nums[i])
            for j in range(i+1,n):
                sums.append(sums[-1]+nums[j])
            
        sums.sort()
        ans=sum(sums[left-1:right])    
        return ans%((10**9) +7)