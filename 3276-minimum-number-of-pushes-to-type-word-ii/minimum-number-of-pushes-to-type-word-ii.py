class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<9:
            return len(word)
        
        dict={}
        ans=0

        for ch in word:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
        sorted_values = sorted(dict.values(), reverse=True)
        print(sorted_values)
        if len(sorted_values)<9:
            return sum(sorted_values)

        # else do some magic
        factor=0
        i=0
        while i<len(sorted_values):
            if i%8 ==0:
                factor+=1
            ans+=(sorted_values[i]*factor)
            # print(f"factor{factor}")
            # print(f"val:{sorted_values}")
            # print(f"ans:{ans}")
            i+=1

        return ans