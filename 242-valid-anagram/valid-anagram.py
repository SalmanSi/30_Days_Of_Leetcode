class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mymap=defaultdict(int)
        for c in s:
            mymap[c]+=1

        for c in t:
            if c not in mymap or mymap[c]==0:
                return False
            else:
                mymap[c]-=1
        return sum(list(mymap.values()))==0       
        
