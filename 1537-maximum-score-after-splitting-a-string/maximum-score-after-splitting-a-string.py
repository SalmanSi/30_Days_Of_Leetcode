class Solution:
    def maxScore(self, s: str) -> int:
        prefixSum0=[0]
        length=len(s)
        for ch in s:
            if ch =='0':
                prefixSum0.append(prefixSum0[-1]+1)
            else:
                prefixSum0.append(prefixSum0[-1])
        print(prefixSum0)

        totalZeros=prefixSum0[-1]

        max_=0
        scores=[]
        for idx,z in enumerate(prefixSum0[1:-1]):
            ones=length-(idx+1)-(totalZeros-z)
            print(f"idx:{idx}")
            print(f"ones:{ones}")
            print(f"zeros:{z}")
            score=z+ones
            print(f"score:{score}")
            scores.append(score)
            max_=max(score,max_)
            print("-------")

        print(scores)
        return max_



        