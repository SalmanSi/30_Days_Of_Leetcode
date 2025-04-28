class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # i,j=0
        # iterate j from 0 to len-1
        # when score[i:j] >k:
        # increment i until score < k
        # then ans+= j-i+1 // the num of sub arrays with j as the right endpoint
        
        res=0
        i=0
        j=0
        arr_sum=0
        for j in range(len(nums)):
            # current sub array total
            arr_sum+=nums[j]

            # current score
            score=arr_sum*(j-i+1)

            # while score > k, remove elments from the left and compute the score again
            while i<=j and score>=k:
                arr_sum-=nums[i]
                i+=1
                # compute new score
                score=arr_sum*(j-i+1)
            
            # when score<k, we have the largest sub array with score<k with the j as the right endpoint
            # so num of valid sub arrays= j-i+1        
            res+=(j-i+1)
        return res