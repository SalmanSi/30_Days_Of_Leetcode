class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        groupToList={}
        
        numToGroup={}
        
        sorted_nums=sorted(nums)
        curGroup=0
        groupToList[curGroup]=[sorted_nums[0]]
        numToGroup[sorted_nums[0]]=curGroup
        for i in range(1,n):
            if sorted_nums[i]-groupToList[curGroup][-1]<=limit:
                groupToList[curGroup].append(sorted_nums[i])
            else:
                curGroup+=1
                groupToList[curGroup]=[sorted_nums[i]]
            numToGroup[sorted_nums[i]]=curGroup
        print(groupToList)
        print(numToGroup)
        
        for i in range(n):
            group=numToGroup[nums[i]]
            nums[i]=groupToList[group].pop(0)
        return nums


       