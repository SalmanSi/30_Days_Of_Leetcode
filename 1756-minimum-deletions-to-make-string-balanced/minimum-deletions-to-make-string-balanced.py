class Solution:
    def minimumDeletions(self, s: str) -> int:
       
        count_a,count_b=0,0
        for c in s:
            if c=='a':
                count_a+=1
            else:
                count_b+=1

        if count_a==0 or count_b==0:
            return 0
        cur_a=0
        cur_b=0
        penalty=[]

        for c in s:

            if c=='a':
                # we consider this is the last 'a'
                # so remove all 'b' before this and all 'a' after this
                
                
                cur_a+=1
                penalty.append(cur_b+count_a-cur_a)
            else:
                penalty.append(cur_b+count_a-cur_a) 
                cur_b+=1
                # we consider this to be the first 'b' in the sequence
                # so we remove all 'b' before this and all' a after this
             

        return min(penalty)
        



        
           
                    