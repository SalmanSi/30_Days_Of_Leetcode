class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones=0
        prefix_ones=[0]*len(boxes)
        idx_sum=0
        prefix_idx_sum=[0]*len(boxes)

        for i in range(len(boxes)):
            if boxes[i]=='1':
                ones+=1
                idx_sum+=i
            prefix_ones[i]=ones
            prefix_idx_sum[i]=idx_sum
        ans=[0]*len(boxes)
        for i in range(len(boxes)):
            if i==0:
                ans[i]=idx_sum
                continue
            elif i==len(boxes)-1 and i>0:
                ans[i]=abs(prefix_idx_sum[i-1]-i*prefix_ones[i-1])
                continue
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