class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans=[]
        card_nums_dict={}
        for num in arr:
            cur=num
            card=0
            while cur>0:
                if cur%2!=0:
                    card+=1
                cur=cur//2
            if card not in card_nums_dict:
                card_nums_dict[card]=[num]
            else:
                card_nums_dict[card].append(num)

        
        card_nums_dict=dict(sorted(card_nums_dict.items()))
        print(card_nums_dict)
        for card,nums in card_nums_dict.items():
            nums.sort()
            ans.extend(nums)
        print(ans)
        return ans