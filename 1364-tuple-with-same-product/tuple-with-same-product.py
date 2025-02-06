class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n=len(nums)
        product_count=defaultdict(int)

        for i in range(n):
            for j in range(i+1,n):
                product_count[nums[i]*nums[j]]+=1
        
        ans=0
        for value in product_count.values():
            if value>1:
                ans+=math.comb(value,2)*8
        return ans
