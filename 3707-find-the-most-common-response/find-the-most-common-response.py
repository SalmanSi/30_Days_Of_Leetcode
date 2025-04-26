class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res_freq={}
        for resp in responses:
            unq_resp = list(dict.fromkeys(resp))
            for res in unq_resp:
                res_freq[res]=res_freq.get(res,0)+1
        res_freq=sorted(res_freq.items(),key=lambda x: (-x[1],x[0]))
        return res_freq[0][0]

        # mymap=defaultdict(int)
        # for resp in responses:
        #     resp=list(set(resp))
        #     for word in resp:
        #         mymap[word]+=1
                    
            
        # mymap=dict(sorted(mymap.items(),key=lambda x: x[0], reverse=False ))
        # mymap=dict(sorted(mymap.items(),key=lambda x: x[1], reverse=True ))
        # return (list(mymap.keys())[0])
 