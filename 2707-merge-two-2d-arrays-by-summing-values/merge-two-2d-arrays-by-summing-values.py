class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # merged=[]
        # c1=0
        # c2=0
        # while c1<len(nums1) and c2<len(nums2):
            
        #     if nums1[c1][0]<nums2[c2][0]:
        #         merged.append(nums1[c1])
        #         c1+=1
        #     elif nums1[c1][0]==nums2[c2][0]:
        #         merged.append([nums1[c1][0],nums1[c1][1]+nums2[c2][1]])
        #         c1+=1
        #         c2+=1
            
        #     elif  nums1[c1][0]>nums2[c2][0]:
        #         merged.append(nums2[c2])
        #         c2+=1
            
        # while c1<len(nums1):
        #     merged.append(nums1[c1])
        #     c1+=1
        # while c2<len(nums2):
        #     merged.append(nums2[c2])   
        #     c2+=1
        # return merged

        id_sum_dict=defaultdict(int)
        for num in nums1:
            id_sum_dict[num[0]]=num[1]
        for num in nums2:
            id_sum_dict[num[0]]+=num[1]
        merged=[]

        for key in sorted(id_sum_dict.keys()):
            merged.append([key,id_sum_dict[key]])
        return merged
