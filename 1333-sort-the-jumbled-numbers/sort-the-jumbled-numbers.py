class Solution:
    def getMapped(self,mapping,num):
        mapped_num=0
        digit_count=1
        if num==0:
            return mapping[0]
        while num>0:
            num,digit=divmod(num,10)
            mapped_num+=mapping[digit]*digit_count
            digit_count*=10
        return mapped_num
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums=[]
        for num in nums:
            mapped_nums.append(self.getMapped(mapping,num))
        my_dict={}

        for i,num in enumerate(mapped_nums):
            my_dict[i]=num
        my_dict=dict(sorted(my_dict.items(), key=lambda item:item[1]))

        indices=list(my_dict.keys())
        mapped_nums=[]
        for index in indices:
            mapped_nums.append(nums[index])
        return mapped_nums