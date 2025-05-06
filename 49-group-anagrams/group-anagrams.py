class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list_map=defaultdict(list)
        for word in strs:
            copy="".join((sorted(word)))
            sorted_list_map[copy].append(word)
        ans=list(sorted_list_map.values())
        return ans



