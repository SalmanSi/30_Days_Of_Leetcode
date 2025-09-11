class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            ans["".join(sorted(s))].append(s)
        
        final=[v for k,v in ans.items()]

        return (final)
        