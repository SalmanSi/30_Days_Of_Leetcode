class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list_map=defaultdict(list)
        for word in strs:
            copy=str(sorted(word))
            sorted_list_map[copy].append(word)
        sorted_list_map=dict(sorted_list_map)
        ans=[]
        for k,v in sorted_list_map.items():
            ans.append(v)
        return ans



