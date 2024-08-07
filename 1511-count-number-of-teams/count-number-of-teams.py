class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # length=len(rating)
        # right_smaller_count=[0]*length
        # left_smaller_count=[0]*length
        # right_larger_count=[0]*length
        # left_larger_count=[0]*length

        # for i in range(0,length):
        #     for j in range(i,length):# right count
        #         if rating[j]>rating[i]:
        #             right_larger_count[i]+=1
        #         elif rating[j]<rating[i]:
        #             right_smaller_count[i]+=1

        #     for j in range(0,i):# left count
        #         if rating[j]>rating[i]:
        #             left_larger_count[i]+=1
        #         elif rating[j]<rating[i]:
        #             left_smaller_count[i]+=1                  

        # ans=0
        # ans+=sum(a*b for a,b in zip(left_smaller_count,right_larger_count))
        # ans+=sum(a*b for a,b in zip(left_larger_count,right_smaller_count))
        # # ans=numpy.dot(left_smaller_count,right_larger_count)+np.dot(left_larger_count,right_smaller_count)
        # return ans

        #more efficient instead of taking dot product
        length=len(rating)
        res=0
        for i,current_rating in enumerate(rating):
                
            right_smaller_count,left_smaller_count=0,0
            right_larger_count,left_larger_count=0,0

            for j in rating[i+1:]:# right count
                if j>current_rating:
                    right_larger_count+=1
                elif j<current_rating:
                    right_smaller_count+=1

            for j in rating[:i]:# left count
                if j>current_rating:
                    left_larger_count+=1
                elif j<current_rating:
                    left_smaller_count+=1  

            res+=left_smaller_count*right_larger_count+left_larger_count*right_smaller_count

        return res