class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        prev_even=(nums[0]%2==0)
        for i in range(1,len(nums)):
            curr_even=(nums[i]%2==0)
            if not(prev_even ^ curr_even):
                return False
            prev_even=curr_even
        return True