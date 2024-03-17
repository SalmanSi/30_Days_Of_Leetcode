class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> dupl;
        int len=nums.size();
        for(int i=0;i<len;i++){
            if(dupl[nums[i]]==1){
                return true;
            }
            dupl[nums[i]]=1;
        }

    return false;
    }
};