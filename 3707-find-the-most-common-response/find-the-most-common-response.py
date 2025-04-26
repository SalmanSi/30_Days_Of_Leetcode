class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        mymap=defaultdict(int)
        for resp in responses:
            resp=list(set(resp))
            for word in resp:
                mymap[word]+=1
                    
            
        mymap=dict(sorted(mymap.items(),key=lambda x: x[0], reverse=False ))
        mymap=dict(sorted(mymap.items(),key=lambda x: x[1], reverse=True ))
        return (list(mymap.keys())[0])
 