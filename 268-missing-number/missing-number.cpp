class Solution {
public:
    int missingNumber(vector<int>& nums) {
  int exp_sum=0,act_sum=0;
  int n=nums.size();
  exp_sum=(n*(n+1))/2;
  for(int num:nums){
    act_sum+=num;
  }
  return exp_sum-act_sum;


        
    }
};