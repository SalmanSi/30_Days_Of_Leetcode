class Solution {
public:

    
    int subsetXORSum(vector<int>& nums) {
        int ans=0;
        for(const int& n:nums){
            ans |=n;
        }
        return ans<<(nums.size()-1);
    }
};