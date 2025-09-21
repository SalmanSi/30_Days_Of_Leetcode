class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=dict(Counter(nums))
        counts=(sorted(counts.items(),key= lambda x : -x[1]))
        ans=[]
        for i in range(k):
            ans.append(counts[i][0])
        return ans
