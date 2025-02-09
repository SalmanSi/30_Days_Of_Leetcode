class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        diff_count=defaultdict(int)
        all_pairs=0
        for i in range(n):
            all_pairs+=i
            diff_count[i-nums[i]]+=1
        
        print(diff_count)
        print(all_pairs)
        good_pairs=0
        for diff,count in diff_count.items():
            if count>1:
                good_pairs+=math.comb(count,2)
        print(good_pairs)
        return all_pairs-good_pairs