class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        int n = nums.size();
        vector<vector<int>> result;
        map<int, int> conjugates;
        int current;
        int target;
        

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n; i++) {
            if(nums[i]>0)
            {
                break;
            }
            
            int duplicate=0;
            if(i>0)
            {
                if(nums[i]==nums[i-1])
                {
                    continue;
                }
            }

            current=nums[i];
            target=-current;
            vector<int>temp;

            for(int j=i+1;j<n;j++)
            {
                 if(j>i+1 && nums[j]==nums[j-1])
                {
                    duplicate+=1;
                }
                if(nums[j]!=nums[j-1])
                {
                    duplicate=0;
                }
                if(duplicate>=2)
                {
                    continue;
                }
                
                if(conjugates.count(nums[j])>0 && i!=j)
                {
                    temp.push_back(current);
                    temp.push_back(nums[j]);
                    temp.push_back(conjugates[nums[j]]);

                    result.push_back(temp);
                    conjugates.erase(nums[j]);
                    temp.clear();
                }else{
                    conjugates[target-nums[j]]=nums[j];
                }
            }
            conjugates.clear();
            temp.clear();
        }
        return result;
    }
};