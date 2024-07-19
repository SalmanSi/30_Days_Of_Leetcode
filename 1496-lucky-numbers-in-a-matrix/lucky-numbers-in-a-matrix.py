class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_list=[]
        max_list=[]

        for row in matrix:
            max_list.append(min(row))
        for i in range(len(matrix[0])):
            col=[row[i] for row in matrix]
            min_list.append(max(col))

        print(max_list)
        print(min_list)
        ans=list(set(min_list)&set(max_list))
        return ans