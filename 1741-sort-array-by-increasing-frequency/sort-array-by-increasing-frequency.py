class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict={}

        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1

        sorted_keys = sorted(dict.keys(), key=lambda k: (dict[k], -k))   

        list=[]
        for key in sorted_keys:
            while dict[key]>0:
                list.append(key)
                dict[key]-=1
        return list

