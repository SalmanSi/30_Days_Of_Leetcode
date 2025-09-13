class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten=[]
        for a in matrix:
            for n in a:
                flatten.append(n)
        mymap=dict(Counter(flatten))
        mymap=dict(sorted(mymap.items()))
        freq=0
        for ke,v in mymap.items():
            freq+=v
            if freq>=k:
                return ke
