class Solution {
public:
    int scoreOfString(string s) {
        int res=0;
        for(auto it=s.begin();it!=s.end();it++){
            if(next(it)!=s.end()){
                res+=abs(*it-*next(it));
            }
        }
        return res;
    }
};