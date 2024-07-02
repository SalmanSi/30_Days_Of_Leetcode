class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        # count map of nums1
        count_map=Counter(nums1)
        ans=[]
      
        for num in nums2:
            if count_map[num]>0:
                ans.append(num)
                count_map[num]-=1


        return ans