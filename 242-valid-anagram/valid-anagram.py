class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap=defaultdict(int)
        tmap=defaultdict(int)
        for c in s:
            smap[c]+=1
        for c in t:
            tmap[c]+=1

        if len(smap.items())!=len(tmap.items()):
            return False
        for k,v in smap.items():
            if tmap[k]!=v:
                return False
        return True