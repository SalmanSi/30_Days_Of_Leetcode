class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list_map={}
        for word in strs:
            copy=str(sorted(word))
            if copy not in sorted_list_map:
                sorted_list_map[copy]=[]
            sorted_list_map[copy].append(word)
        ans=[]
        for k,v in sorted_list_map.items():
            ans.append(v)
        return ans



