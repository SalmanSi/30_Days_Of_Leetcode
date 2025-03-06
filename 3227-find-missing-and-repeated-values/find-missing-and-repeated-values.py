class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rows=len(grid)
        cols=len(grid[0])
        flat_nums=[0]*(rows*cols)
        repeated=-1
        counter=0
        all_sum=0
        cur_sum=0
        for row in grid:
            for num in row:
                counter+=1
                cur_sum+=num
                all_sum+=counter
                if flat_nums[num-1]!=0:
                    repeated=num
                flat_nums[num-1]=num
        missing=all_sum-(cur_sum-repeated)

        return [repeated,missing]