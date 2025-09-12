class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=nums.count(val)

        s=0
        e=len(nums)-1
        while s<e:
            while nums[e]==val and e>s:
                e-=1
            if nums[s]==val:
                nums[s],nums[e]=nums[e],nums[s]
            s+=1
            print(nums)
        return len(nums)-k

                
                