class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes=list(dominoes)

        mylist=[]
        for idx,d in enumerate(dominoes):
            if d!='.':
                mylist.append((d,idx))
        print(mylist)
        if len(mylist)==1:
            first=mylist[0]
            if first[0]=='L':
                for j in range(0,first[1]):
                    dominoes[j]='L'
            else:
                for j in range(first[1],len(dominoes)):
                    dominoes[j]='R'    
        for i in range(len(mylist)-1):
            first=mylist[i]
            second=mylist[i+1]
            # 4 cases:
            # 1- L-L
            if first[0]=='L' and second[0]=='L':
                if i==0:
                    for j in range(0,first[1]):
                        dominoes[j]='L'
                for j in range(first[1],second[1]):
                    dominoes[j]='L'
            # 2- L-R
            elif first[0]=='L' and second[0]=='R':
                if i==0:
                    for j in range(0,first[1]):
                        dominoes[j]='L'
                if i==len(mylist)-2:
                    for j in range(second[1],len(dominoes)):
                        dominoes[j]='R'          
            # 3- R-R
            elif first[0]=='R' and second[0]=='R':
                for j in range(first[1],second[1]):
                    dominoes[j]='R'
                if i==len(mylist)-2:
                    for j in range(second[1],len(dominoes)):
                        dominoes[j]='R'
            # 4- R-L          
            elif first[0]=='R' and second[0]=='L':
                between=(second[1]-first[1]-1)//2
                for j in range(1,between+1):
                    dominoes[first[1]+j]='R'
                    dominoes[second[1]-j]='L'
                

        print(dominoes)
        return ''.join(map(str,dominoes))
