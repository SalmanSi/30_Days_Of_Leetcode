class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> dupl;
        int len=nums.size();
        for(const auto& num:nums){
            if(dupl[num]==1){
                return true;
            }
            dupl[num]=1;
        }

    return false;
    }
};