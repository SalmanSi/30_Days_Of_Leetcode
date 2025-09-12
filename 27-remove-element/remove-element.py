class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end=len(nums)-1
        nums.sort()
        k=len(nums)-nums.count(val)
        for i in range(len(nums)):
            if nums[i]==val and i<end:
                nums[i],nums[end]=nums[end],nums[i]
                end-=1
        return k
                

       
            