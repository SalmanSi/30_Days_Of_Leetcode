class Solution:
    def getMapped(self,mapping,num):
        mapped=0
        digits=[int(digit) for digit in str(num)]
        for digit in digits:
            mapped=mapped*10+mapping[digit]
        return mapped
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