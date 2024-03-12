class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>result;
        int prd=1;
        for(int num:nums){
            result.push_back(prd);//product before
            prd*=num;
        }
        prd=1;

        for(auto it_n=nums.rbegin(),it_r=result.rbegin();it_n!=nums.rend();++it_n,++it_r){
            *it_r=*it_r * prd;
            prd*=*it_n;
        }
        return result;
    }
    
};