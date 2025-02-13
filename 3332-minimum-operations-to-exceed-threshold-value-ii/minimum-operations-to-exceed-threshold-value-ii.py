class Solution:


    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        heapq.heapify(nums)
        while nums[0]<k:
            ans+=1
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            heapq.heappush(nums,2*x+y)
        return ans
