class Solution:
    def check(self, nums: List[int]) -> bool:
        first=False
        


        for i in range(len(nums)):
            if nums[(i+1)%len(nums)]<nums[i]:
                if not first:
                    first=True
                else:
                    return False
            
        return True