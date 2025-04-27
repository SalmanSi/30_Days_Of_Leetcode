class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # More optimal approach
        # approach:- 
        # - for each row and col, find the max and min entries
        # - all the points between the max and min are covered on 2 sides, we need to check the 
        #   remaining
        #   2 sides
        # - traverse each building and check if its row is between max and min and if its col is
        #   between max and min. 
        # - If true, ans+=1
        max_r=[float('-inf')]*n
        min_r=[float('inf')]*n
        max_c=[float('-inf')]*n
        min_c=[float('inf')]*n

        for r,c in buildings:
            r-=1
            c-=1
            max_r[r]=max(max_r[r],c)
            min_r[r]=min(min_r[r],c)
            max_c[c]=max(max_c[c],r)
            min_c[c]=min(min_c[c],r)
        
        ans=0
        for r,c in buildings:
            r-=1
            c-=1
            if min_c[c]<r<max_c[c] and min_r[r]<c<max_r[r]:
                ans+=1
        return ans



        # def getTuples(axis,list_,myset,row=True):
        #     for item in list_:
        #         if row:
        #             myset.add((axis,item))
        #         else:
        #             myset.add((item,axis))

        # # sort by rows and then cols
        # buildings.sort(key=lambda x: (x[0],x[1]))

        # # build the rows dict and rows set
        # row_set=set()
        # row_dict=defaultdict(list)
        # for r,c in buildings:
        #     row_dict[r].append(c)

        # # sort by cols then rows 
        # buildings.sort(key=lambda x:(x[1],x[0]))

        # # build the cols dict and cols set
        # col_set=set()
        # col_dict=defaultdict(list)

        # for r,c in buildings:
        #     col_dict[c].append(r)
        # # print(row_dict)
        # # print(col_dict)
        # for r,cols in row_dict.items():
        #     if len(cols)>2:
        #         getTuples(r,cols[1:-1],row_set,True)
        
        # for c,rows in col_dict.items():
        #     if len(rows)>2:
        #         getTuples(c,rows[1:-1],col_set,False)
        # return len(row_set.intersection(col_set))