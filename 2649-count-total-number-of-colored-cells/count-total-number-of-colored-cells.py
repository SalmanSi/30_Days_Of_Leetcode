class Solution:
    def coloredCells(self, n: int) -> int:
        
        middle=1+(n-1)*2
        top=(n-1)**2
        return 2*top+middle
