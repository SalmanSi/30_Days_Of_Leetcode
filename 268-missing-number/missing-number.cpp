class Solution {
public:
    int missingNumber(vector<int>& nums) {
    int result=nums[0];
    int len=nums.size();
    for(int i=1;i<len;i++){
       result^=nums[i];
       result^=i;
    }
    result^=len;
    return result;


        
    }
};