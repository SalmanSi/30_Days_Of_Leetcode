class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        def getTuples(axis,list_,myset,row=True):
            for item in list_:
                if row:
                    myset.add((axis,item))
                else:
                    myset.add((item,axis))

        # sort by rows and then cols
        buildings.sort(key=lambda x: (x[0],x[1]))

        # build the rows dict and rows set
        row_set=set()
        row_dict=defaultdict(list)
        for r,c in buildings:
            row_dict[r].append(c)

        # sort by cols then rows 
        buildings.sort(key=lambda x:(x[1],x[0]))

        # build the cols dict and cols set
        col_set=set()
        col_dict=defaultdict(list)

        for r,c in buildings:
            col_dict[c].append(r)
        # print(row_dict)
        # print(col_dict)
        for r,cols in row_dict.items():
            if len(cols)>2:
                getTuples(r,cols[1:-1],row_set,True)
        
        for c,rows in col_dict.items():
            if len(rows)>2:
                getTuples(c,rows[1:-1],col_set,False)
        return len(row_set.intersection(col_set))