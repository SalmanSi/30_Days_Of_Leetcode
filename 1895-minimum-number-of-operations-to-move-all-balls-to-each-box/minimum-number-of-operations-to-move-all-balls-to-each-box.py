class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones=0
        prefix_ones=[0]*len(boxes)
        idx_sum=0
        prefix_idx_sum=[0]*len(boxes)
        # instead of using 2 arrays (postfix and prefix from right and left)
        # use a prefix sum array for ones and sum of idx where 1 and subtract from total to
        # get the values on right
        for i in range(len(boxes)):
            # construct comm count arrays for number of ones and sum of idxs where 1
            if boxes[i]=='1':
                ones+=1
                idx_sum+=i
            prefix_ones[i]=ones
            prefix_idx_sum[i]=idx_sum


        ans=[0]*len(boxes)
        for i in range(len(boxes)):
            # for the first index, answer = sum of 1 indexes
            if i==0:
                ans[i]=idx_sum
                continue
            # for the last element, use sum of n-1 th elment and subtract from it the last idex * number of ones seen on left to adjust for the distance FROM the last index
            elif i==len(boxes)-1 and i>0:
                ans[i]=abs(prefix_idx_sum[i-1]-i*prefix_ones[i-1])
                continue

            # for elements in the mid, compute both right and left sums
            left=abs(prefix_idx_sum[i-1]-i*prefix_ones[i-1])
            right=(idx_sum-prefix_idx_sum[i])-i*(ones-prefix_ones[i])
            ans[i]=left+right
        return ans



        # very inefficient solution- O(n*n)
        # ans=[0]*len(boxes)

        # for i in range(len(boxes)):
        #     for j in range(len(boxes)):
        #         if i==j:
        #             continue
        #         if boxes[j]=='1':
        #             ans[i]+=abs(i-j)
        # return ans