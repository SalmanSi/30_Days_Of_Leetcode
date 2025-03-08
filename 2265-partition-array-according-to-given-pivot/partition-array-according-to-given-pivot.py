class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser=[]
        equal=[]
        greater=[]
        for n in nums:
            if n<pivot:
                lesser.append(n)
            elif n==pivot:
                equal.append(n)
            else:
                greater.append(n)
        return lesser+equal+greater