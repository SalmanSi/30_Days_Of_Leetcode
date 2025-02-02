class Solution:
    def check(self, nums: List[int]) -> bool:
        first=False
        
        for i in range(-1, len(nums)-1 ):
            if nums[(i+1)]<nums[i]:
                if first:
                    return False
                first= True
        
        # for i in range(len(nums)):
        #     if nums[(i+1)%len(nums)]<nums[i]:
        #         if first:
        #             return False
        #         first= True
        
           
        return True