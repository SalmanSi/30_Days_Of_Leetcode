class Solution {
public:
    int missingNumber(vector<int>& nums) {
    int result=0;
    int len=nums.size();
    for(int i=0;i<len;i++){
       result^=nums[i]^i;
    }
    result^=len;
    return result;


        
    }
};