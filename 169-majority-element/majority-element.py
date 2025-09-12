class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        map=dict(Counter(nums))
        for k,v in map.items():
            if v>n:
                return k
        