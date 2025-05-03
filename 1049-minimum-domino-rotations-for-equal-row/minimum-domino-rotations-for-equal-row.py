class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_freq_map=Counter(tops)
        # sort by freq in descending order
        top_freq_map=dict(sorted(top_freq_map.items(),key=lambda x: x[1], reverse=True))
        
        bottom_freq_map=Counter(bottoms)
        bottom_freq_map=dict(sorted(bottom_freq_map.items(),key=lambda x:x[1],reverse=True))
        print(top_freq_map)
        print(bottom_freq_map)

        overlap_map=defaultdict(int)
        for i in range(len(tops)):
            if tops[i]==bottoms[i]:
                overlap_map[tops[i]]+=1
        overlap_map=dict(overlap_map)
        print(overlap_map)

        ans=[]
        size=len(tops)
        # iterate over both the maps and get the possible answers
        for val,freq in top_freq_map.items():
            if freq+bottom_freq_map.get(val,0)-overlap_map.get(val,0)>=size:
                ans.append(size-freq)
        for val,freq in bottom_freq_map.items():
            if freq+top_freq_map.get(val,0)-overlap_map.get(val,0)>=size:
                ans.append(size-freq)
        
        if len(ans)==0:
            return -1
        else: 
            return min(ans)


        return 0