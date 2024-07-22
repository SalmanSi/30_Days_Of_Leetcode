class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict={}

        for i in range(len(names)):
            dict[heights[i]]=names[i]

        heights.sort(reverse=True)

        ans=[]
        for h in heights:
            ans.append(dict[h])
        return ans