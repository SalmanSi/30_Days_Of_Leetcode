class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=copy.deepcopy(matrix)
        r=len(matrix)
        c=len(matrix[0])
        for rr in range(0,r):
            for cc in range(0,c):
                if cc>0:
                    self.matrix[rr][cc]+=self.matrix[rr][cc-1]
        for rr in range(0,r):
            for cc in range(0,c):
                if rr>0:
                    self.matrix[rr][cc]+=self.matrix[rr-1][cc]
        print(self.matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        final_sum=self.matrix[row2][col2]
        initial_sum=0
        if row1>0:
            rr=row1-1
            initial_sum+=self.matrix[rr][col2]

        if col1>0:
            cc=col1-1
            initial_sum+=(self.matrix[row2][cc])
            if row1>0:
                initial_sum-=self.matrix[row1-1][cc]
        print(final_sum)
        print(initial_sum)
        return final_sum-initial_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)