class Solution {
public:
    static bool compare(const int &a, const int &b){
        return a>b;
    }
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(),happiness.end(),compare);
        int len=happiness.size();
        long long sum=0;
        //int turn=0;
        for(int i=0;i<k;i++){
            if(happiness[i]-i>=0){
                sum+=happiness[i]-i;
            }else{break;}
            
            
        }
        
        return sum;
    }
};