class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int expected_sum=(n*(n+1))/2;
        int actual_sum=0;
        for(int num:nums){
            actual_sum+=num;
        }
        int res=expected_sum-actual_sum;
        if(res>0){
            return res;
        }
        return 0;


        
    }
};