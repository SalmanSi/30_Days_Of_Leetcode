class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        dict={}
        for idx,num in enumerate(nums):
            if target-num not in dict:
                dict[num]=idx
            else:
                ans.append(dict[target-num])
                ans.append(idx)
                return ans
        