class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size=len(nums)
        ans=[0]*size
        for i in range(size):
            ans[i]=nums[nums[i]]
        return ans