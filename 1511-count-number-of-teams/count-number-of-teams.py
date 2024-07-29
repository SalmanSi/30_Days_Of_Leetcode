class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length=len(rating)
        right_smaller_count=[0]*length
        left_smaller_count=[0]*length
        right_larger_count=[0]*length
        left_larger_count=[0]*length

        for i in range(0,length):
            for j in range(0,length):
                if j>i:#right larger_count
                    if rating[j]>rating[i]:
                        right_larger_count[i]+=1
                    elif rating[j]<rating[i]:
                        right_smaller_count[i]+=1
                elif j<i:#left larger count
                    if rating[j]>rating[i]:
                        left_larger_count[i]+=1
                    elif rating[j]<rating[i]:
                        left_smaller_count[i]+=1

        ans=0
        ans+=sum(a*b for a,b in zip(left_smaller_count,right_larger_count))
        ans+=sum(a*b for a,b in zip(left_larger_count,right_smaller_count))
        # ans=numpy.dot(left_smaller_count,right_larger_count)+np.dot(left_larger_count,right_smaller_count)
        return ans

