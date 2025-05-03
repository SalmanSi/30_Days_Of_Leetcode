class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # greedy solution
        ans=float('inf')
        # check for all nums:
        for x in range(1,7):
            topCount=0
            bottomCount=0
            for i in range(len(tops)):
                if tops[i]!=x and bottoms[i]!=x:
                    topCount=bottomCount=-1
                    break # this x is not possible
                if tops[i]!=x:
                    topCount+=1
                if bottoms[i]!=x:
                    bottomCount+=1
            
            if topCount!=-1 and bottomCount!=-1:
                ans=min(ans,topCount,bottomCount)
            

        print(ans)
        if ans==float('inf'):
            return -1
        else:
            return ans
        
                

        
        # top_freq_map=Counter(tops)
        # # sort by freq in descending order
        # top_freq_map=dict(sorted(top_freq_map.items(),key=lambda x: x[1], reverse=True))
        
        # bottom_freq_map=Counter(bottoms)
        # bottom_freq_map=dict(sorted(bottom_freq_map.items(),key=lambda x:x[1],reverse=True))

        # overlap_map=defaultdict(int)
        # for i in range(len(tops)):
        #     if tops[i]==bottoms[i]:
        #         overlap_map[tops[i]]+=1
        # overlap_map=dict(overlap_map)

        # ans=[]
        # size=len(tops)
        # # iterate over both the maps and get the possible answers
        # for val,freq in top_freq_map.items():
        #     if freq+bottom_freq_map.get(val,0)-overlap_map.get(val,0)>=size:
        #         ans.append(size-freq)
        # for val,freq in bottom_freq_map.items():
        #     if freq+top_freq_map.get(val,0)-overlap_map.get(val,0)>=size:
        #         ans.append(size-freq)
        
        # if len(ans)==0:
        #     return -1
        # else: 
        #     return min(ans)


        return 0